package com.example.sulmun2




import android.annotation.SuppressLint
import android.content.Intent
import android.media.Image
import android.os.Bundle
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity



class Survey_2 : AppCompatActivity() {
    @SuppressLint("SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.sulmun2)

        var count1 = 0
        var nextpage1: TextView
        var back_1 : ImageView
        var rg5: RadioGroup
        var rg6: RadioGroup
        var rg7: RadioGroup
        var rg8: RadioGroup


        var count123 = 0

       back_1 = findViewById<ImageView>(R.id.back_1)
        rg5 = findViewById<RadioGroup>(R.id.rg5)
        rg6 = findViewById<RadioGroup>(R.id.rg6)
        rg7 = findViewById<RadioGroup>(R.id.rg7)
        rg8 = findViewById<RadioGroup>(R.id.rg8)
        val nextpage2 = findViewById<TextView>(R.id.nextpage2)
        rg5.setOnCheckedChangeListener { Radiogroup, checkedId ->

            when (checkedId) {
                R.id.radio21 -> count1 += 2;
                R.id.radio22 -> count1 += 4;
                R.id.radio23 -> count1 += 6;
                R.id.radio24 -> count1 += 8;
                R.id.radio25 -> count1 += 10;


            }
        }

        rg6.setOnCheckedChangeListener { Radiogroup, checkedId ->

            when (checkedId) {
                R.id.radio26 -> count1 += 2;
                R.id.radio27 -> count1 += 4;
                R.id.radio28 -> count1 += 6;
                R.id.radio29 -> count1 += 8;
                R.id.radio30 -> count1 += 10;


            }

        }

        rg7.setOnCheckedChangeListener { Radiogroup, checkedId ->

            when (checkedId) {
                R.id.radio31 -> count1 += 2;
                R.id.radio32 -> count1 += 4;
                R.id.radio33 -> count1 += 6;
                R.id.radio34 -> count1 += 8;
                R.id.radio35 -> count1 += 10;
            }

        }
        rg8.setOnCheckedChangeListener { Radiogroup, checkedId ->

            when (checkedId) {
                R.id.radio36 -> count1 += 2;
                R.id.radio37 -> count1 += 4;
                R.id.radio38 -> count1 += 6;
                R.id.radio39 -> count1 += 8;
                R.id.radio40 -> count1 += 10;


            }


        }

        back_1.setOnClickListener {

            var intent = Intent(this,Survey::class.java)
            startActivity(intent)
        }


        nextpage2.setOnClickListener {
            var countfinal1 = intent.getIntExtra("JUMSU", 0)
            count123 = countfinal1 + count1
            val intent = Intent(this, Survey_3::class.java)
            intent.putExtra("JUMSU1", count123.toInt())


            startActivity(intent)

        }
    }

    }

