var express = require('express');
const session = require('express-session');
var router = express.Router();

const User = require('../module/User');
const Course = require('../module/Course');
const Result = require('../module/Result');
const { v4 } = require('uuid');

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});
router.post('/login', function(req, res, next) {

  if (req.body.id == 'admin') {
    res.redirect('/users/admin');
    return;
  }
  if (typeof req.session.users == 'undefined') {
    req.session.users = [];
    res.send(new Result(1, '가입되어 있지 않은 회원입니다.'));
    return;
  }
  var users = req.session.users;
  for (var i = 0; i < users.length; i++) {
    if (users[i].id == req.body.id) {
      if (users[i].password == req.body.password) {
        req.session.login_user = users[i];
        res.send(new Result(0, '인증에 성공하였습니다.'));
        return;
      } else {
        res.send(new Result(2, '비밀번호가 일치하지 않습니다.'));
        return;
      }
    }
  }
  res.send(new Result(1, '가입되어 있지 않은 회원입니다.'));
});
router.post('/joinproc', function(req, res, next) {
  console.log(req.session);
  if (typeof req.session.users == 'undefined') {
    req.session.users = [];
  }
  var users = req.session.users;
  for (var i = 0; i < users.length; i++) {
    if (users[i].id == req.body.id) {
      res.render('index', { title: 'Express' });
    }
  }
  req.session.users.push(new User(req.body.id, req.body.password1));
  res.render('index', { title: 'Express' });
});
router.get('/join', function(req, res, next) {
  res.render('join', { title: 'Express' });
});

router.post('/course_add', function(req, res, next) {
  if (typeof req.session.courses == 'undefined') {
    req.session.courses = [];
  }
  var idx = v4();
  var name = req.body.course;

  req.session.courses.push(new Course(idx, name, null));
  res.redirect('/users/admin')
});
router.get('/course_delete', function(req, res, next) {
  if (typeof req.session.courses == 'undefined') {
    req.session.courses = [];
  }
  for (var i = 0; i < req.session.courses.length; i++) {
      if (req.session.courses[i].idx == req.query.idx) {
        req.session.courses.splice(i, 1);
        res.redirect('/users/courses');
        return;
      }
  }
  res.redirect('/users/admin');
});
router.get('/user_course_add', function(req, res, next) {
  if (typeof req.session.courses == 'undefined') {
    req.session.courses = [];
  }
  for (var i = 0; i < req.session.courses.length; i++) {
    if (req.session.courses[i].idx == req.query.idx) {
      if (req.session.courses[i].User == null) {
        req.session.courses[i].User = [];
      }
      req.session.courses[i].User.push(req.session.login_user);
      res.redirect('/users/courses');
      return;
    }
  }
  console.debug(req.session.courses);
  res.redirect('/users/courses');
});
router.get('/user_course_delete', function(req, res, next) {
  if (typeof req.session.courses == 'undefined') {
    req.session.courses = [];
  }
  for (var i = 0; i < req.session.courses.length; i++) {
    if (req.session.courses[i].idx == req.query.idx) {
      for (var j = 0; j < req.session.courses[i].User.length; j++) {
        if (req.session.courses[i].User[j].id == req.session.login_user.id) {
          req.session.courses[i].User.splice(j, 1);
        }
      }
      res.redirect('/users/courses');
      return;
    }
  }
  console.debug(req.session.courses);
  res.redirect('/users/courses');
});
router.get('/admin', function(req, res, next) {

  var courses = [];
  if (typeof req.session.courses != 'undefined') {
    courses = req.session.courses;
  }
  res.render('admin', { courses: courses });
});
router.get('/courses', function(req, res, next) {

  var courses = [];
  if (typeof req.session.courses != 'undefined') {
    courses = req.session.courses;
  }
  res.render('course', { courses: courses, login_user: req.session.login_user });
});
module.exports = router;
