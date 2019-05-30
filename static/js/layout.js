window.addEventListener("scroll",function() {
    const header = document.getElementById('header');
    const logo = document.getElementById('logo');
    const wrapper = document.getElementById('wrapper');
    const banner = document.getElementById('banner');
    const bannerTitle = document.getElementById('bannerTitle');
    const goUp = document.getElementById('goUp');

    if(window.pageYOffset>0){
        header.style.height="80px";
        logo.style.height="60px";
        header.style.background="tomato";
        banner.style.lineHeight="80px";
        wrapper.style.paddingTop="80px";
        bannerTitle.style.color="#00cec9";
    }
    else{
        header.style.height="120px";
        logo.style.height="100px";
        header.style.background="#0abde3";
        banner.style.lineHeight="120px";
        wrapper.style.paddingTop="120px";
        bannerTitle.style.color="#d63031";
    }
    if(window.pageYOffset>150){
        goUp.style.display="block";
    }
    else{
        goUp.style.display="none";
    }
});