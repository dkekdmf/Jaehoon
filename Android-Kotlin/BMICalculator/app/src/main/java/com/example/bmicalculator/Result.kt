package com.example.bmicalculator

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class Result : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.result)

        val ResultBmi : TextView = findViewById(R.id.ResultBMI)
        val Result : TextView = findViewById(R.id.Result)
        val ReusltBmi2 : TextView = findViewById(R.id.ResultBMI1)
        val Result1 : TextView = findViewById(R.id.Result1)
        val height1 = intent.getIntExtra("height",0)
        val weight1 = intent.getIntExtra("weight",0)



       val bmi = weight1/ Math.pow(height1/100.0, 2.0)

        val resultText = when{
            bmi >= 35.0 -> "고도 비만"
            bmi >= 30.0 -> "중경도 비만"
            bmi >=25.0 -> "경도 비만"
            bmi >= 23.0 -> "과체중"
            bmi >= 18.5 -> "정상체중"
            else -> "저체중"
        }
        Result.text = bmi.toString()
        Result1.text = resultText.toString()

    }
}

