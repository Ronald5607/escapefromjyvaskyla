class Airplane {
    constructor(imgurl, ctx, map) {
        this.img = this.makeimg(imgurl);
        //world lat/lon
        this.lat = 62.4034;
        this.lon = 25.6810;

        //canvas context used to draw the airplane
        this.ctx = ctx;

        this.map = map;
        
        this.rotation = 0;

        //canvas coordinates (pixels)
        this.x = 0;
        this.y = 0;
        this.setcanvascoordinates();

    }
    
    setcanvascoordinates() {
        let coords = this.map.latLngToContainerPoint([this.lat, this.lon]);
        this.x = coords.x - 100;
        this.y = coords.y - 100;
    }

    makeimg(imgurl) {
        const img = document.createElement('img');

        img.addEventListener('error', (err) => {
            console.log(err);
        });
    img.setAttribute('src', imgurl);
    return img;
    }

    initairplane() {
    
    /* this.rotation = 1; */

    this.img.addEventListener("load", () => {
        this.ctx.save();
        this.ctx.translate(this.x, this.y);
        ctx.drawImage(this.img, 0, 0);
        this.ctx.restore();
    });

    }

    changerotation(target, t) {
        let delta = this.rotation - target;
        this.rotation = this.rotation + delta*t;
    }

    rotateairplane() {
        this.ctx.translate(100, 100);
        this.ctx.rotate(this.rotation);
        this.ctx.translate(-100, -100);
    }
    
    scaleairplane() {
        this.ctx.translate(100, 100);
        this.ctx.scale(0.3, 0.3);
        this.ctx.translate(-100, -100);
    }

    draw() {
        clearcanvas();
        this.ctx.save();
        this.ctx.translate(this.x, this.y);
        this.rotateairplane();
        this.scaleairplane();
        this.ctx.drawImage(this.img, 0, 0);
        this.ctx.restore();
        window.requestAnimationFrame(() => {this.draw()});

    }
    }