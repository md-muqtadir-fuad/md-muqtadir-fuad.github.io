// server/routes/projectRoutes.js
const express = require('express');
const router = express.Router();
const { getProjects, getProjectById, createProject} = require('../controllers/projectController');

//map the routes to the controller functions

router.get('/', getProjects); // GET /api/projects
router.get('/:id', getProjectById);// GET /api/projects/12345
router.post('/', createProject); // POST /api/projects

module.exports = router;