<?php include('header.php'); ?>

<!-- Navigation -->
<?php include('nav.php'); ?>

<!-- Hero Section -->
<section id="hero" class="hero">
    <div>
        <h2>Welcome to My Modern Webpage</h2>
        <p>Building innovative solutions with modern design.</p>
        <a href="#contact" class="cta-btn">Get Started</a>
    </div>
</section>

<!-- About Section -->
<section id="about" class="about">
    <h2>About Us</h2>
    <p>We specialize in creating websites that are not only visually appealing but also highly functional and user-friendly.</p>
</section>

<!-- Features Section -->
<section id="features" class="features">
    <div class="feature-item">
        <h3>Responsive Design</h3>
        <p>Optimized for desktops, tablets, and smartphones.</p>
    </div>
    <div class="feature-item">
        <h3>Fast Performance</h3>
        <p>Speed optimization for quick loading and smooth experience.</p>
    </div>
    <div class="feature-item">
        <h3>SEO Optimized</h3>
        <p>Built with search engine optimization in mind for better rankings.</p>
    </div>
</section>

<!-- Testimonials Section -->
<section id="testimonials" class="testimonials">
    <h2>What Our Clients Say</h2>
    <div class="testimonial-item">
        <p>"This team transformed our website into something extraordinary!"</p>
        <p>- Sarah Williams</p>
    </div>
    <div class="testimonial-item">
        <p>"Amazing service! Our website has seen significant improvements!"</p>
        <p>- John Doe</p>
    </div>
</section>

<!-- Blog Section -->
<section id="blog" class="blog">
    <h2>Our Latest Blog Posts</h2>
    <div class="blog-post">
        <h3>Web Design Trends for 2025</h3>
        <p>Learn about the latest web design trends.</p>
    </div>
    <div class="blog-post">
        <h3>SEO Best Practices</h3>
        <p>Explore SEO techniques to enhance your website's visibility.</p>
    </div>
</section>

<!-- Contact Section -->
<section id="contact" class="contact">
    <h2>Contact Us</h2>
    <form action="submit_contact.php" method="POST">
        <input type="text" name="name" placeholder="Your Name" required><br>
        <input type="email" name="email" placeholder="Your Email" required><br>
        <textarea name="message" placeholder="Your Message" required></textarea><br>
        <button type="submit">Send Message</button>
    </form>
</section>

<!-- Footer -->
<?php include('footer.php'); ?>

<script src="scripts.js"></script>
</body>
</html>
