package com.example.sulmun2


import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity


class Survey_4 : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.sulmun4)

        var count11 = 0
        var countfn1  = 0
        var horrorchange : Button
        var typeresult : TextView
        var tresult : TextView

        var back_1 : ImageView
        var horrorchange1 : Button
        var atype : View
        var btype : View
        var ctype : View
        atype = findViewById<View>(R.id.atype)
        btype = findViewById<View>(R.id.btype)
        ctype = findViewById<View>(R.id.ctype)
        horrorchange1 = findViewById<Button>(R.id.horrorchange1)

        var textresult : TextView
         tresult = findViewById<TextView>(R.id.tresult)
        typeresult = findViewById<TextView>(R.id.typeresult)

        textresult = findViewById<TextView>(R.id.result)


        countfn1 = intent.getIntExtra("JUMSU2", 0)

        back_1 = findViewById<ImageView>(R.id.back_1)

        textresult.text = " 당신의 공포심리 테스트 점수는" + countfn1.toString() + "점입니다"

        if (countfn1 <= 30) {
            typeresult.text = "축하합니다. 당신은 강철의 심장!! "
            tresult.text = "A타입을 추천합니다. "

        } else if (countfn1 > 30 && countfn1 < 70) {
            typeresult.text ="밤에 어두운 곳을 가기 싫으신가요?"
            tresult.text = "B타입을 추천합니다."

        } else if (countfn1 >= 70) {
            typeresult.text = "밤 길에 누가 쫓아오는 것 같나요? "
            tresult.text = "C타입을 추천합니다."


        }
        horrorchange1.setOnClickListener {

            var intent = Intent(this,MainActivity::class.java)
            startActivity(intent)
        }


        back_1.setOnClickListener {

            var intent = Intent(this,Survey_3::class.java)
            startActivity(intent)
        }


        atype.setOnClickListener {

            var intent = Intent(this,horror1::class.java)
            startActivity(intent)
        }
        btype.setOnClickListener {

            var intent = Intent(this,horror2::class.java)
            startActivity(intent)
        }
        ctype.setOnClickListener {

            var intent = Intent(this,horror3::class.java)
            startActivity(intent)
        }










        }}





