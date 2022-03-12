
package com.example.sulmun2






import android.content.Intent
import android.os.Bundle
import android.telephony.RadioAccessSpecifier
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity

import com.example.sulmun2.R
import com.example.sulmun2.Survey_4
import org.w3c.dom.Text


class Survey_3 : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.sulmun3)
        var count  = 0;
        var textresult : TextView
        var rg9 : RadioGroup
        var rg10 : RadioGroup
        var count1234 = 0
        var countfinal12  : Int =0
        var count123 : Int = 0
        var count1 : Int = 0
        var finish1 : TextView
        var back_1 : ImageView

        rg9 = findViewById<RadioGroup>(R.id.rg9)
        rg10 = findViewById<RadioGroup>(R.id.rg10)
        finish1 = findViewById<TextView>(R.id.finish1)
        back_1 = findViewById<ImageView>(R.id.back_1)
        rg9.setOnCheckedChangeListener { Radiogroup, checkedId ->

            when (checkedId) {
                R.id.radio41 -> count += 2;
                R.id.radio42 -> count += 4;
                R.id.radio43 -> count += 6;
                R.id.radio44 -> count += 8;
                R.id.radio45 -> count += 10;


            }
        }
        rg10.setOnCheckedChangeListener { Radiogroup, checkedId ->

            when (checkedId) {
                R.id.radio46 -> count += 2;
                R.id.radio47 -> count += 4;
                R.id.radio48 -> count += 6;
                R.id.radio49 -> count += 8;
                R.id.radio50 -> count += 10;


            }

        }





        finish1.setOnClickListener {

            countfinal12 = intent.getIntExtra("JUMSU1", 0)
            count1234 = countfinal12 + count

            val intent = Intent(this, Survey_4::class.java)
            intent.putExtra("JUMSU2", count1234.toInt())

            startActivity(intent)
        }

        back_1.setOnClickListener {

            var intent = Intent(this,Survey_2::class.java)
            startActivity(intent)
        }




        //  textresult.text = " 점수는? " + count.toString()




    }}