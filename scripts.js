document.addEventListener("DOMContentLoaded", () => {
    const links = document.querySelectorAll("nav ul li a");

    links.forEach(link => {
        link.addEventListener("click", (event) => {
            // event.preventDefault();
            const sectionId = link.getAttribute("href").substring(1);
            const section = document.getElementById(sectionId);

            window.scrollTo({
                top: section.offsetTop,
                behavior: 'smooth'
            });
            // loadAboutContent();
        });
    });
})

// function loadAboutContent() {

//     const aboutSection = document.getElementById('about');
//     aboutSection.innerHTML =`
//     <h2>About Me</h2>
//         <p>Hi, I'm Yash. I'm currently studying Statistics and Data Science at UCLA.
//         While I did build this site myself, it's probably pretty clear that web development isn't my strong suit.
//         My interests lie more in data analysis and visualization (see <a href="#projects">projects</a> to learn more). 
//         This is about the extent of my web development skills.</p>
//         `;
    
// }
