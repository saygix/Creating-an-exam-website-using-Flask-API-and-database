document.addEventListener('DOMContentLoaded', function () {
    const posts = document.querySelectorAll('article');
    
    posts.forEach(post => {
        post.classList.add('fade-in');
    });
});
