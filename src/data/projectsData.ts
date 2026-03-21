export const projectsData = [
  {
    id: 1,
    slug: 'egov-lens',
    title: 'eGov-Lens',
    category: 'Machine Learning / NLP',
    shortDescription: 'Multi-dimensional ML approach for aspect-based public feedback analysis on Bengali e-Gov platforms.',
    overview: 'This project focuses on analyzing public feedback on e-government platforms in Bangladesh using advanced NLP techniques. We developed a multi-dimensional ML model to categorize feedback into various aspects and sentiments, providing actionable insights for policy makers.',
    tools: ['Python', 'PyTorch', 'Transformers', 'Scikit-learn'],
    highlights: [
      'Developed a custom dataset of Bengali e-gov feedback.',
      'Achieved high accuracy in aspect extraction and sentiment classification.',
      'Presented at ICCIT 2025.'
    ],
    links: [
      { label: 'ResearchGate', url: 'https://www.researchgate.net/profile/Md-Muqtadir-Fuad' }
    ]
  },
  {
    id: 2,
    slug: 'smart-conveyor',
    title: 'IoT-Based Smart Conveyor',
    category: 'IoT / Industrial Engineering',
    shortDescription: 'Integrated quality, inventory, and process control system using IoT.',
    overview: 'A smart conveyor system designed for real-time monitoring of manufacturing processes. It integrates sensors and IoT modules to track quality metrics, inventory levels, and process efficiency.',
    tools: ['Arduino', 'Raspberry Pi', 'Node.js', 'MQTT'],
    highlights: [
      'Real-time data visualization dashboard.',
      'Automated quality rejection mechanism.',
      'Reduced process downtime by 15%.'
    ],
    links: [
      { label: 'Poster', url: 'https://doi.org/10.13140/RG.2.2.25476.23683' }
    ]
  }
];
