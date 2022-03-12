package com.example.sulmun2

import android.content.Intent
import android.os.Bundle
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import com.example.sulmun2.horror2detail.*
import com.example.sulmun2.horror3detail.*

class horror3 : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.horror3)


        var back_1 : ImageView

        var click1 : ImageView
        var click2 : ImageView
        var click3 : ImageView
        var click4 : ImageView
        var click5 : ImageView
        var click6 : ImageView
        var click7 : ImageView
        var click8 : ImageView
        var click9 : ImageView
        var click10 : ImageView
        var click11 : ImageView
        var click12 : ImageView
        var click13 : ImageView
        var click14 : ImageView
        var click15: ImageView
        var click16 : ImageView
        back_1 = findViewById<ImageView>(R.id.back_1)
        click1 = findViewById<ImageView>(R.id.image33)
        click2 = findViewById<ImageView>(R.id.image34)
        click3 = findViewById<ImageView>(R.id.image35)
        click4 = findViewById<ImageView>(R.id.image36)
        click5 = findViewById<ImageView>(R.id.image37)
        click6 = findViewById<ImageView>(R.id.image38)
        click7 = findViewById<ImageView>(R.id.image39)
        click8 = findViewById<ImageView>(R.id.image40)
        click9 = findViewById<ImageView>(R.id.image41)
        click10 = findViewById<ImageView>(R.id.image42)
        click11 = findViewById<ImageView>(R.id.image43)
        click12 = findViewById<ImageView>(R.id.image44)
        click13 = findViewById<ImageView>(R.id.image45)
        click14 = findViewById<ImageView>(R.id.image46)
        click15= findViewById<ImageView>(R.id.image47)
        click16 = findViewById<ImageView>(R.id.image48)


        back_1.setOnClickListener {

            intent = Intent(applicationContext,Survey_4::class.java)
            startActivity(intent)
        }
        click1.setOnClickListener{

            intent = Intent(applicationContext, horrordetail33::class.java)
            startActivity(intent)

        }

        click2.setOnClickListener{

            intent = Intent(applicationContext, horrordetail34::class.java)
            startActivity(intent)

        }


        click3.setOnClickListener{

            intent = Intent(applicationContext, horrordetail35::class.java)
            startActivity(intent)

        }


        click4.setOnClickListener{

            intent = Intent(applicationContext, horrordetail36::class.java)
            startActivity(intent)

        }


        click5.setOnClickListener{

            intent = Intent(applicationContext, horrordetail37::class.java)
            startActivity(intent)

        }


        click6.setOnClickListener{

            intent = Intent(applicationContext, horrordetail38::class.java)
            startActivity(intent)

        }


        click7.setOnClickListener{

            intent = Intent(applicationContext, horrordetail39::class.java)
            startActivity(intent)

        }


        click8.setOnClickListener{

            intent = Intent(applicationContext, horrordetail40::class.java)
            startActivity(intent)

        }


        click9.setOnClickListener{

            intent = Intent(applicationContext, horrordetail41::class.java)
            startActivity(intent)

        }


        click10.setOnClickListener{

            intent = Intent(applicationContext, horrordetail42::class.java)
            startActivity(intent)

        }


        click11.setOnClickListener{

            intent = Intent(applicationContext, horrordetail43::class.java)
            startActivity(intent)

        }


        click12.setOnClickListener{

            intent = Intent(applicationContext, horrordetail44::class.java)
            startActivity(intent)

        }


        click13.setOnClickListener{

            intent = Intent(applicationContext, horrordetail45::class.java)
            startActivity(intent)

        }


        click14.setOnClickListener{

            intent = Intent(applicationContext, horrordetail46::class.java)
            startActivity(intent)

        }


        click15.setOnClickListener{

            intent = Intent(applicationContext, horrordetail47::class.java)
            startActivity(intent)

        }


        click16.setOnClickListener{

            intent = Intent(applicationContext, horrordetail48::class.java)
            startActivity(intent)

        }































    }}