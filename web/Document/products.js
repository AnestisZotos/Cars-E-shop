const API_BASE_URL = 'http://127.0.0.1:5000';

function getImageFilename(productName) {
    if (productName.toLowerCase().includes('mini cooper')) {
        return 'minicooper.png';
    }
    return productName.toLowerCase().split(' ').pop() + '.png';
}

async function handleSearch() {
    const searchInput = document.querySelector('.search-bar');
    const searchTerm = searchInput.value.trim();
    
    try {
        const url = searchTerm ? 
            `${API_BASE_URL}/search?name=${encodeURIComponent(searchTerm)}` :
            `${API_BASE_URL}/search`;
            
        const response = await fetch(url);
        const products = await response.json();
        
        const productsGrid = document.querySelector('.products-grid');
        productsGrid.innerHTML = '';
        
        products.forEach(product => {
            const carCard = document.createElement('div');
            carCard.className = 'car-card';
            
            const imageName = getImageFilename(product.name);
            
            carCard.innerHTML = `
                <img src="images/${imageName}" alt="${product.name}" class="product-image">
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <p class="price">€${product.price.toLocaleString()}</p>
                <p class="likes">Likes: ${product.likes || 0}</p>
                <a href="#" class="buy-button">Buy Now</a>
            `;
            
            const productImage = carCard.querySelector('.product-image');
            productImage.addEventListener('click', () => handleLike(product._id));
            
            productsGrid.appendChild(carCard);
        });
    } catch (error) {
        console.error('Error searching products:', error);
    }
}

async function handleLike(productId) {
    try {
        const response = await fetch(`${API_BASE_URL}/like`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: productId })
        });
        
        if (response.ok) {
            handleSearch();
        }
    } catch (error) {
        console.error('Error liking product:', error);
    }
}

async function loadPopularProducts() {
    try {
        const response = await fetch(`${API_BASE_URL}/popular-products`);
        const popularProducts = await response.json();

        const slideshow = document.querySelector('#slideshow');
        slideshow.innerHTML = '';

        popularProducts.slice(0, 5).forEach(product => {
            const slide = document.createElement('div');
            slide.className = 'slide fade';

            const imageName = getImageFilename(product.name);
            slide.innerHTML = `
                <img src="images/${imageName}" alt="${product.name}">
                <div class="slide-caption">${product.name}</div>
            `;
            slideshow.appendChild(slide);
        });

        const firstSlide = document.querySelector('.slide');
        if (firstSlide) {
            firstSlide.classList.add('active');
        }
    } catch (error) {
        console.error('Error loading popular products:', error);
    }
}

function startSlideshow() {
    let slides = document.querySelectorAll('.slide');
    let currentSlide = 0;

    setInterval(() => {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active');
    }, 3000);
}

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.querySelector('.search-bar');
    if (searchInput) {
        searchInput.addEventListener('input', handleSearch);
        handleSearch();
    }

    if (window.location.pathname.includes('homepage.html')) {
        loadPopularProducts().then(startSlideshow);
    }
});
