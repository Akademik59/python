document.addEventListener('DOMContentLoaded', () => {
    const contHead = document.querySelector('.cont_header');
    const scrollBtn = document.querySelector('.scroll_top');
    const header = document.querySelector('.header');
    

    window.addEventListener('scroll', () => {
        let scrollTop = window.scrollY;
        let contHeadTop = contHead.offsetHeight;

        if (scrollTop >= contHeadTop) {
            scrollBtn.classList.add('active');
        } else{
            scrollBtn.classList.remove('active');
        }
        
    });

    scrollBtn.addEventListener('click', function(){
        scrollTo(header)
    })

    function scrollTo(element){
        window.scroll({
            left: 0,
            top: element.offsetTop,
            behavior: "smooth"
        });
    };

    


});