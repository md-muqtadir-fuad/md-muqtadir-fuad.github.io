// server/controllers/projectController.js

const Project = require('../models/Project');

//@desc Get all projects
//@route GET /api/projects
//fetching all projects
const getProjects = async (req, res) => {
    try {
        const projects = await Project.find().sort({ createdAt: -1 });
        res.status(200).json(projects);
    } catch (error) {
        res.status(500).json({ message: "Server Error", error: error.message });
    }
};

//Fetching a single project for a Details page
const getProjectById = async (req, res) => {
    try {
        const project = await Project.findById(req.params.id);
        if (!project) {
            return res.status(404).json({ message: "Project not found" });
        }
        res.status(200).json(project);
    } catch (error) {
        res.status(500).json({ message: "Server error", error: error.message });
    }
}

// @desc Create a nes project
//@route POST /api/projects

const createProject = async (req, res) => {
    try {
        //req.body contains the json data sent from the front end or postman
        const { title, description, imageUrl, technologies, githubLink, liveLink } = req.body;
        const newProject = new Project({
            title,
            description,
            imageUrl,
            technologies,
            githubLink,
            liveLink
        });

        // .save() is Mongoose's version of INSERT INTO

        const savedProject = await newProject.save();
        res.status(201).json(savedProject);
    } catch (error) {
        res.status(400).json({ message: "Failed to create project", error: error.message });

    }
};

module.exports = { getProjects, getProjectById, createProject };