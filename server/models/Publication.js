const mongose = require('mongoose');

const publicationSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
    },
    publisher: {
        type: String, // eg "IEEE"
    },
    datePublished: {
        type: Date,
    },
    link: {
        type: String,
    },
    imageUrl: {
        type: String,
        default: "", // can add a placeholder image link here later
    },
    abstract: {
        type: String,
        required: true,
    },

    keywords: {
        type: [String], // Array of strings, e.g., ["React", "Node", "MongoDB"]
        required: true,
    },
    detailedContent: {
        type: String, // Long description/content for dedicated Details page
    }

});

module.exports = mongoose.model('Publication', publicationSchema);