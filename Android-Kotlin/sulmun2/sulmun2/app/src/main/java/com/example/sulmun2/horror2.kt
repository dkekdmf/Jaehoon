package com.example.sulmun2

import android.content.Intent
import android.os.Bundle
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import com.example.sulmun2.horror2detail.*
import com.example.sulmun2.horrordetail.*

class horror2 : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.horror2)


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
        click1 = findViewById<ImageView>(R.id.image17)
        click2 = findViewById<ImageView>(R.id.image18)
        click3 = findViewById<ImageView>(R.id.image19)
        click4 = findViewById<ImageView>(R.id.image20)
        click5 = findViewById<ImageView>(R.id.image21)
        click6 = findViewById<ImageView>(R.id.image22)
        click7 = findViewById<ImageView>(R.id.image23)
        click8 = findViewById<ImageView>(R.id.image24)
        click9 = findViewById<ImageView>(R.id.image25)
        click10 = findViewById<ImageView>(R.id.image26)
        click11 = findViewById<ImageView>(R.id.image27)
        click12 = findViewById<ImageView>(R.id.image28)
        click13 = findViewById<ImageView>(R.id.image29)
        click14 = findViewById<ImageView>(R.id.image30)
        click15= findViewById<ImageView>(R.id.image31)
        click16 = findViewById<ImageView>(R.id.image32)


        back_1.setOnClickListener {

            intent = Intent(applicationContext,Survey_4::class.java)
            startActivity(intent)
        }
        click1.setOnClickListener{

            intent = Intent(applicationContext, horrordetail17::class.java)
            startActivity(intent)

        }

        click2.setOnClickListener{

            intent = Intent(applicationContext, horrordetail18::class.java)
            startActivity(intent)

        }


        click3.setOnClickListener{

            intent = Intent(applicationContext, horrordetail19::class.java)
            startActivity(intent)

        }


        click4.setOnClickListener{

            intent = Intent(applicationContext, horrordetail20::class.java)
            startActivity(intent)

        }


        click5.setOnClickListener{

            intent = Intent(applicationContext, horrordetail21::class.java)
            startActivity(intent)

        }


        click6.setOnClickListener{

            intent = Intent(applicationContext, horrordetail22::class.java)
            startActivity(intent)

        }


        click7.setOnClickListener{

            intent = Intent(applicationContext, horrordetail23::class.java)
            startActivity(intent)

        }


        click8.setOnClickListener{

            intent = Intent(applicationContext, horrordetail24::class.java)
            startActivity(intent)

        }


        click9.setOnClickListener{

            intent = Intent(applicationContext, horrordetail25::class.java)
            startActivity(intent)

        }


        click10.setOnClickListener{

            intent = Intent(applicationContext, horrordetail26::class.java)
            startActivity(intent)

        }


        click11.setOnClickListener{

            intent = Intent(applicationContext, horrordetail27::class.java)
            startActivity(intent)

        }


        click12.setOnClickListener{

            intent = Intent(applicationContext, horrordetail28::class.java)
            startActivity(intent)

        }


        click13.setOnClickListener{

            intent = Intent(applicationContext, horrordetail29::class.java)
            startActivity(intent)

        }


        click14.setOnClickListener{

            intent = Intent(applicationContext, horrordetail30::class.java)
            startActivity(intent)

        }


        click15.setOnClickListener{

            intent = Intent(applicationContext, horrordetail31::class.java)
            startActivity(intent)

        }


        click16.setOnClickListener{

            intent = Intent(applicationContext, horrordetail32::class.java)
            startActivity(intent)

        }




















    }}