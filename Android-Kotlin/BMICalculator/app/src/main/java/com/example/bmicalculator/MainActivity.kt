package com.example.bmicalculator

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val Height : EditText = findViewById(R.id.height)
        val Weight : EditText = findViewById(R.id.weight)
        val calculator = findViewById<Button>(R.id.calculator)

        calculator.setOnClickListener {

            val height = Height.text.toString().toInt()
            val weight = Weight.text.toString().toInt()
          var intent = Intent(this,Result::class.java)
            intent.putExtra("height",height)
            intent.putExtra("weight",weight)
           startActivity(intent)
        }




    }
}