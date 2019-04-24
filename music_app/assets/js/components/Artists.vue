<template>
 <div v-bind:style="home" class="home1">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <nav v-bind:style='slide' class="slidemenu">
            <!-- Item 1 -->
            <input type="radio" name="slideItem" id="slide-item-1" class="slide-toggle" />
            <label for="slide-item-1"><a href='/home'><p class="icon">♬</p><span>Charts</span></a></label>
            
            <!-- Item 2 -->
            <input type="radio" name="slideItem" id="slide-item-2" class="slide-toggle" />
            <label for="slide-item-2"><a href='/albums'><p class="icon"><i class="fa fa-clone" style="font-size:30px"></i></p><span>Albums</span></a></label>
            
            <!-- Item 3 -->
            <input type="radio" name="slideItem" id="slide-item-3" class="slide-toggle" checked/>
            <label for="slide-item-3"><a href='/artists'><p class="icon"><i class="fa fa-headphones" style="font-size:36px"></i></p><span>Artists</span></a></label>
            
            <!-- Item 4 -->
            <input type="radio" name="slideItem" id="slide-item-4" class="slide-toggle"/>
            <label for="slide-item-4"><a href='/'><p class="icon"><i class='fa fa-cogs' style="font-size: 32px"></i></p><span>Logout</span></a></label>
            
            <!--<div class="clear"></div> -->
            
            <!-- Bar -->
           <!-- <div v-bind:style='slider' class="slider">
                <div class="bar"></div>
            </div> -->
        </nav>
        <div v-bind:style='gr' class="grid-container">
          <div class="item1"><i><a href='https://www.youtube.com/channel/UC-6czyMkxDi8E8akPl0c7_w' class='i1'>Enrique Igleasis</a></i></div>
          <div class="item2"><i><a href='https://www.youtube.com/channel/UC0C-w0YjGpqDXGB8IHb662A' class='i1'>Ed Sheeran</a></i></div>
          <div class="item3"><i><a href='https://www.youtube.com/channel/UCb2HGwORFBo94DmRx4oLzow' class='i1'>One Direction</a></i></div>  
          <div class="item4"><i><a href='https://www.youtube.com/channel/UC9CoOnJkIBMdeijd9qYoT_g' class='i2'>Ariana Grande</a></i></div>
          <div class="item5"><i><a href='https://www.youtube.com/channel/UCV5Gw7GGOMxe6SSF6llp_3Q' class='i1'>James Arthur</a></i></div>
          <div class="item6"><i><a href='https://www.youtube.com/channel/UCvpDeGlR5wLP9Z3Tb6K0Xfg' class ='i1'>Sam Smith</a></i></div>
        </div>
    </div>
</template>

<script>
export default{
data() {
    return{
        gr: {
                opacity: 0.8,
                display: 'grid',
                gridTemplateColumns: 'auto auto auto',
                gridGap: '10px',
                backgroundColor: 'rgba(143, 233, 155, 0.979)',
                padding: '10px',
        },
        home:{
                width: '100%',
                height: '100%',
                margin: 0,
                padding: 0,
                fontFamily: 'sans-serif',
                backgroundSize: 'cover',
                backgroundPosition: 'center',
        },
        slide: {
                    fontFamily: 'arial, sans-serif',
                    width: '100%',
                    overflow: 'hidden',
        },
        /*slider: {
                width: '100%',
                height: '5px',
                display: 'block',
                background: '#ccc',
                marginTop: '10px',
                borderRadius: '5px',
        }*/
    }
}
}
</script>
<style type= 'text/css' scoped>
.i1{
  font-weight: bold;
  color: white;
}
.i2{
  font-weight: bold;
  color: black;
}
.item1{
   background: url(enrique.jpg); 
 }
 .item2{
   background: url(ed.jpg);
 }
 .item3{
   background: url(1D.jpg);
 }
 .item4{
   background: url(ariana.jpg);
 }
 .item5{
   background: url(james.jpg);
 }
 .item6{
   background: url(sam.jpg);
 }
 .grid-container > div {
  color: white;
  background-color: black;
  text-align: center;
  padding: 100px 0;
  font-size: 30px;
}

.item1 {
  grid-column-start: 1;
  grid-column-end: 1;
}
.home1{
   
    background: url(bg1.jpg);
   
}
.clear{
  clear: both;
}
.slide-toggle{
  display: none;
}
.slidemenu label{
  width: 25%;
  text-align: center;
  display: block;
  float: left;
  color: #333;
  opacity: 0.2;

}
.slidemenu label:hover{
  cursor: pointer;
  color: #666;
}
.slidemenu label span{
  display: block;
  padding: 10px;    
}
.slidemenu label .icon{
  font-size: 20px;
  border: solid 2px #333;
  text-align: center;
  height: 50px;
  width: 50px;
  display: block;
  margin: 0 auto;
  line-height: 50px;
  border-radius: 50%;
}

.slider .bar{
  width: 25%;
  height: 5px;
  background: #333;
  border-radius: 5px;
}
.slidemenu label, .slider .bar {
  transition: all 500ms ease-in-out;
  -webkit-transition: all 500ms ease-in-out;
  -moz-transition: all 500ms ease-in-out;
}
.slidemenu .slide-toggle:checked + label{
  opacity: 1;
}
.slidemenu #slide-item-1:checked ~ .slider .bar{ margin-left: 0; }
.slidemenu #slide-item-2:checked ~ .slider .bar{ margin-left: 25%; }
.slidemenu #slide-item-3:checked ~ .slider .bar{ margin-left: 50%; }
.slidemenu #slide-item-4:checked ~ .slider .bar{ margin-left: 75%; }
</style>