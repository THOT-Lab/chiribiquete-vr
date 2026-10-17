document.addEventListener('DOMContentLoaded', () => {
  // Barra superior: fondo al desplazarse
  const topbar = document.querySelector('[data-topbar]');
  const onScroll = () => topbar.classList.toggle('is-scrolled', window.scrollY > 40);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Aparición progresiva de los bloques
  const items = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach((el) => io.observe(el));
  } else {
    items.forEach((el) => el.classList.add('is-in'));
  }

  // Friso de pictogramas: se duplica para un desfile continuo
  const track = document.querySelector('.frieze__track');
  if (track) track.innerHTML += track.innerHTML;

  // Video de entrada: bucle automático con fundido en cada vuelta
  document.querySelectorAll('video[data-fadeloop]').forEach((video) => {
    const FADE = 0.6;
    const play = () => video.play().catch(() => {});
    video.addEventListener('timeupdate', () => {
      if (video.duration && video.duration - video.currentTime < FADE) video.classList.add('is-fading');
    });
    video.addEventListener('ended', () => {
      video.currentTime = 0;
      play();
      requestAnimationFrame(() => video.classList.remove('is-fading'));
    });
    // Solo se reproduce cuando está visible
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([entry]) => {
        if (entry.isIntersecting) play(); else video.pause();
      }, { threshold: 0.2 }).observe(video);
    } else {
      play();
    }
  });

  // Galería: imagen ampliada
  const lightbox = document.querySelector('[data-lightbox]');
  const gallery = document.querySelector('[data-gallery]');
  if (lightbox && gallery && typeof lightbox.showModal === 'function') {
    const big = lightbox.querySelector('img');
    gallery.addEventListener('click', (event) => {
      const img = event.target.closest('.gallery__item')?.querySelector('img');
      if (!img) return;
      big.src = img.currentSrc || img.src;
      big.alt = img.alt;
      lightbox.showModal();
    });
    lightbox.addEventListener('click', () => lightbox.close());
  }
});
