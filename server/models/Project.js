const mongoose = require('mongoose');
const projectSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
    },
    description: {
        type: String,
        required: true,
    },
    imageUrl: {
        type: String,
        default: "", // can add a placeholder image link here later
    },
    technologies: {
        type: [String], // Array of strings, e.g., ["React", "Node", "MongoDB"]
        required: true,
    },
    githubLink: {
        type: String,
    },
    liveLink: {
        type: String,
    },
},
    { timestamps: true } // automatically add areatedAt and updatedAt dates
);

module.exports = mongoose.model('Project', projectSchema);