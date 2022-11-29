package com.example.arrow_blink

import android.os.Bundle
import android.view.View
import android.view.animation.Animation
import android.view.animation.AnimationUtils
import android.widget.Button
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        var arrow1 : ImageView
        var arrow2 : ImageView
        var leftButton : Button
        var rightButton : Button
        var centerButton : Button
        var speedView : ImageView
        var OffleftButton : Button
        var OffRightButton : Button
        var OffCenterButton : Button
        arrow1 = findViewById<ImageView>(R.id.arrow1)
        arrow2 = findViewById<ImageView>(R.id.arrow2)
        leftButton = findViewById<Button>(R.id.leftButton)

        OffleftButton = findViewById<Button>(R.id.OffleftButton)
        rightButton = findViewById<Button>(R.id.rightButton)
        OffRightButton = findViewById<Button>(R.id.OffrightButton)
        centerButton = findViewById<Button>(R.id.centerButton)
        OffCenterButton = findViewById<Button>(R.id.OffcenterButton)
        speedView = findViewById<ImageView>(R.id.SpeedView)


        leftButton.setOnClickListener {


                var anim = AnimationUtils.loadAnimation(applicationContext,R.anim.blink_2)
                arrow2.startAnimation(anim)


        }
        OffleftButton.setOnClickListener {


            arrow2.clearAnimation()


        }
        rightButton.setOnClickListener {


            var anim = AnimationUtils.loadAnimation(applicationContext,R.anim.blink_2)
            arrow1.startAnimation(anim)



        }
        OffRightButton.setOnClickListener {

                 arrow1.clearAnimation()



        }


        centerButton.setOnClickListener {


            var anim = AnimationUtils.loadAnimation(applicationContext,R.anim.blink_2)
            arrow1.startAnimation(anim)
            arrow2.startAnimation(anim)

    }
        OffCenterButton.setOnClickListener {
            //overridePendingTransition(0,0)
            arrow1.clearAnimation()
            arrow2.clearAnimation()
            // var anim = AnimationUtils.loadAnimation(applicationContext,R.anim.blink_2)
            // arrow1.startAnimation(anim)
            // arrow2.startAnimation(anim)

        }



}

    override fun onPause() {
        super.onPause()
        overridePendingTransition(0,0)
    }


}