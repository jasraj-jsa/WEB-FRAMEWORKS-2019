<template>
    <div v-bind:style="home" class="home1">
        <nav class="slidemenu">
            <!-- Item 1 -->
            <input type="radio" name="slideItem" id="slide-item-1" class="slide-toggle" />
            <label for="slide-item-1"><a href='../'><p class="icon">♬</p><span>Home</span></a></label>
            
            <!-- Item 2 -->
            <input type="radio" name="slideItem" id="slide-item-2" class="slide-toggle" checked/>
            <label for="slide-item-2"><a href='/features'><p class="icon">★</p><span>Features</span></a></label>
            
            <!-- Item 3 -->
            <input type="radio" name="slideItem" id="slide-item-3" class="slide-toggle"/>
            <label for="slide-item-3"><a href='/premium'><p class="icon">✈</p><span>Premium</span></a></label> 
            
            <!-- Item 4 -->
            <input type="radio" name="slideItem" id="slide-item-4" class="slide-toggle"/>
            <label for="slide-item-4"><a href='/about'><p class="icon">✎</p><span>About</span></a></label>
            
            <div class="clear"></div>
            
            <!-- Bar -->
            <div v-bind:style="slider" class="slider">
                <div class="bar"></div>
            </div>
        </nav>
        <div class = 'wrapper'>
          <h1> <u>Features</u> </h1>
          <h3> Our Features Include:
            <div> Your Library </div>
            <div> Shuffle Play </div>
            <div> Download music and podcasts </div>
            <div> Mello Radio </div>
            <div> View Lyrics </div>
            <div> Play Queue And History </div>
        </h3>
        </div>
    </div>
</template>

<script>
export default{
    data(){
      return{
        home:{
                width: '100%',
                height: '100%',
                margin: 0,
                padding: 0,
                fontFamily: 'sans-serif',
                backgroundSize: 'cover',
                backgroundPosition: 'center',
        },
        slider: {
                width: '100%',
                height: '5px',
                display: 'block',
                background: '#ccc',
                marginTop: '10px',
                borderRadius: '5px',
        }
      }
    }
}
</script>

<style type='text/css' scoped>
.wrapper > h1{
  font-weight: bold;
  align-self: center;
  align-content: center;
  text-align: center;
}
.wrapper{ 
    align-content: center;
    margin-right: auto; 
    margin-left:  auto; 
    background-color: #F8E609;
    opacity:0.8;
    max-width: 550px;
    color: black;
    padding-right: 10px; 
    padding-left:  10px; 
}
.home1{
    background: url(logo.png);
}

.clear{
  clear: both;
}


.slide-toggle{
  display: none;
}

.slidemenu{
  font-family: arial, sans-serif;
  width: 100%;
  overflow: hidden;
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

/*Animations*/
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
