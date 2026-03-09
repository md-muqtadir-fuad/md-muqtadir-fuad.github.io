//server/config/db.js
const mongoose = require('mongoose');

const connectDB = async () => {
    try {
        //connect to moongoseDB using the env file
        await mongoose.connect(process.env.MONGO_URI);
        console.log('MongoDB connecetion successfull :0');
    } catch(error){
        console.error('MongoDB connecetion failed :|');
        console.error(error.message);
        process.exit(1); //stop the server if the database doesn't connect
    }
};

module.exports = connectDB;