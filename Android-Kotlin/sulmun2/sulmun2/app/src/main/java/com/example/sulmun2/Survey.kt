package com.example.sulmun2


import android.content.Intent
import android.os.Bundle
import android.widget.*
import androidx.appcompat.app.AppCompatActivity


class Survey : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.sulmun1)

        var count2 = 0;

        var countfinal = 0
        var rg1: RadioGroup
        var rg2: RadioGroup
        var rg3: RadioGroup
        var rg4: RadioGroup
        var back_1 : ImageView

        back_1 = findViewById<ImageView>(R.id.back_1)
        rg1 = findViewById<RadioGroup>(R.id.rg1)
        rg2 = findViewById<RadioGroup>(R.id.rg2)
        rg3 = findViewById<RadioGroup>(R.id.rg3)
        rg4 = findViewById<RadioGroup>(R.id.rg4)
        var nextpage = findViewById<TextView>(R.id.nextpage00)


        rg1.setOnCheckedChangeListener { Radiogroup, checkedId ->


            when (checkedId) {
                R.id.radio1 -> count2 += 2;
                R.id.radio2 -> count2 += 4;
                R.id.radio3 -> count2 += 6;
                R.id.radio4 -> count2 += 8;
                R.id.radio5 -> count2 += 10;


            }
        }
        rg2.setOnCheckedChangeListener { Radiogroup, checkedId ->

            when (checkedId) {
                R.id.radio6 -> count2 += 2;
                R.id.radio7 -> count2 += 4;
                R.id.radio8 -> count2 += 6;
                R.id.radio9 -> count2 += 8;
                R.id.radio10 -> count2 += 10;


            }

        }

        rg3.setOnCheckedChangeListener { Radiogroup, checkedId ->

            when (checkedId) {
                R.id.radio11 -> count2 += 2;
                R.id.radio12 -> count2 += 4;
                R.id.radio13 -> count2 += 6;
                R.id.radio14 -> count2 += 8;
                R.id.radio15 -> count2 += 10;
            }

        }
        rg4.setOnCheckedChangeListener { Radiogroup, checkedId ->

            when (checkedId) {
                R.id.radio16 -> count2 += 2;

                R.id.radio17 -> count2 += 4;
                R.id.radio18 -> count2 += 6;
                R.id.radio19 -> count2 += 8;
                R.id.radio20 -> count2 += 10;


            }
        }
        back_1.setOnClickListener {

            var intent = Intent(this,MainActivity::class.java)
            startActivity(intent)
        }
        nextpage.setOnClickListener {
            val intent = Intent(this, Survey_2::class.java)
            intent.putExtra("JUMSU", count2.toInt())


            startActivity(intent)

        }


    }}