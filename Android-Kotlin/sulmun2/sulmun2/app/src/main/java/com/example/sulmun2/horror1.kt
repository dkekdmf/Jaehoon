package com.example.sulmun2

import android.content.Intent
import android.os.Bundle
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import com.example.sulmun2.horrordetail.*

class horror1 : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.horror1)


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
        var back_1 : ImageView
        back_1 = findViewById<ImageView>(R.id.back_1)
        click1 = findViewById<ImageView>(R.id.image1)
        click2 = findViewById<ImageView>(R.id.image2)
        click3 = findViewById<ImageView>(R.id.image3)
        click4 = findViewById<ImageView>(R.id.image4)
        click5 = findViewById<ImageView>(R.id.image5)
        click6 = findViewById<ImageView>(R.id.image6)
        click7 = findViewById<ImageView>(R.id.image7)
        click8 = findViewById<ImageView>(R.id.image8)
        click9 = findViewById<ImageView>(R.id.image9)
        click10 = findViewById<ImageView>(R.id.image10)
        click11 = findViewById<ImageView>(R.id.image11)
        click12 = findViewById<ImageView>(R.id.image12)
        click13 = findViewById<ImageView>(R.id.image13)
        click14 = findViewById<ImageView>(R.id.image14)
        click15= findViewById<ImageView>(R.id.image15)
        click16 = findViewById<ImageView>(R.id.image16)

        back_1.setOnClickListener {

            intent = Intent(applicationContext,Survey_4::class.java)
            startActivity(intent)
        }




        click1.setOnClickListener{

            intent = Intent(applicationContext,horrordetail1::class.java)
            startActivity(intent)

        }

        click2.setOnClickListener{

            intent = Intent(applicationContext, horrordetail2::class.java)
            startActivity(intent)

        }


        click3.setOnClickListener{

            intent = Intent(applicationContext, horrordetail3::class.java)
            startActivity(intent)

        }


        click4.setOnClickListener{

            intent = Intent(applicationContext, horrordetail4::class.java)
            startActivity(intent)

        }


        click5.setOnClickListener{

            intent = Intent(applicationContext, horrordetail5::class.java)
            startActivity(intent)

        }


        click6.setOnClickListener{

            intent = Intent(applicationContext,horrordetail6::class.java)
            startActivity(intent)

        }


        click7.setOnClickListener{

            intent = Intent(applicationContext,horrordetail7::class.java)
            startActivity(intent)

        }


        click8.setOnClickListener{

            intent = Intent(applicationContext,horrordetail8::class.java)
            startActivity(intent)

        }


        click9.setOnClickListener{

            intent = Intent(applicationContext,horrordetail9::class.java)
            startActivity(intent)

        }


        click10.setOnClickListener{

            intent = Intent(applicationContext,horrordetail10::class.java)
            startActivity(intent)

        }


        click11.setOnClickListener{

            intent = Intent(applicationContext,horrordetail11::class.java)
            startActivity(intent)

        }


        click12.setOnClickListener{

            intent = Intent(applicationContext,horrordetail12::class.java)
            startActivity(intent)

        }


        click13.setOnClickListener{

            intent = Intent(applicationContext,horrordetail13::class.java)
            startActivity(intent)

        }


        click14.setOnClickListener{

            intent = Intent(applicationContext,horrordetail14::class.java)
            startActivity(intent)

        }


        click15.setOnClickListener{

            intent = Intent(applicationContext,horrordetail15::class.java)
            startActivity(intent)

        }


        click16.setOnClickListener{

            intent = Intent(applicationContext,horrordetail16::class.java)
            startActivity(intent)

        }
















    }}
