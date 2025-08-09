package com.example.travelapp

import android.os.Bundle
import android.widget.*
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var etDestination: EditText
    private lateinit var etDate: EditText
    private lateinit var etBudget: EditText
    private lateinit var tvItinerary: TextView
    private lateinit var tvTrackingStatus: TextView
    private lateinit var etExpenseName: EditText
    private lateinit var etExpenseAmount: EditText
    private lateinit var tvExpensesList: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Trip planning
        etDestination = findViewById(R.id.etDestination)
        etDate = findViewById(R.id.etDate)
        etBudget = findViewById(R.id.etBudget)
        tvItinerary = findViewById(R.id.tvItinerary)

        findViewById<Button>(R.id.btnCreateItinerary).setOnClickListener {
            val destination = etDestination.text.toString()
            val date = etDate.text.toString()
            val budget = etBudget.text.toString()
            tvItinerary.text = "Trip to $destination on $date with a budget of $$budget."
        }

        // Trip tracking
        tvTrackingStatus = findViewById(R.id.tvTrackingStatus)
        findViewById<Button>(R.id.btnStartTracking).setOnClickListener {
            tvTrackingStatus.text = "✅ Tracking started..."
        }

        // Expense manager
        etExpenseName = findViewById(R.id.etExpenseName)
        etExpenseAmount = findViewById(R.id.etExpenseAmount)
        tvExpensesList = findViewById(R.id.tvExpensesList)

        findViewById<Button>(R.id.btnAddExpense).setOnClickListener {
            val name = etExpenseName.text.toString()
            val amount = etExpenseAmount.text.toString()
            val currentText = tvExpensesList.text.toString()
            tvExpensesList.text = "$currentText\n$name: $$amount"
            etExpenseName.text.clear()
            etExpenseAmount.text.clear()
        }
    }
}
