package com.example.morninghospital2

import android.content.Intent
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ImageView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val netflix = findViewById<ImageView>(R.id.netflix)
        val coupang = findViewById<ImageView>(R.id.coupang)
        val watcha = findViewById<ImageView>(R.id.watcha)
        val tving = findViewById<ImageView>(R.id.tving)

        netflix.setOnClickListener {
            intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://www.netflix.com/kr/"))
            startActivity(intent)

        }
        coupang.setOnClickListener {
            intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://www.coupangplay.com/"))
            startActivity(intent)
        }
        watcha.setOnClickListener {
            intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://watcha.com/"))
            startActivity(intent)
        }
        tving.setOnClickListener {
            intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://www.tving.com/"))
            startActivity(intent)
        }
    }
}