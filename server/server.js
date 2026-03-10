// server/server.js
const express = require('express');
const cors = require('cors');
require('dotenv').config();
const connectDB = require('./config/db'); //import db connection
const projectRoutes = require('./routes/projectRoutes');

const app =express();
const PORT = process.env.PORT || 5000;

connectDB(); //connect to database

app.use(cors());
app.use(express.json());

// Add the Project Routes
app.use('/api/projects', projectRoutes);//tells express to use them

app.get('/api', (req, res) => {
    res.json({message:"Welcome to the portfolio API"});
})

app.listen(PORT,() =>{
    console.log(`Server is running on port: ${PORT}`);
})