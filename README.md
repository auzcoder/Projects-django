# <p class="django">Django ~  Pyhton </p>
<h1 style="color: #0d7f3a">  </h1>

<div class="wraper">
	<div class='str'></div>
	<div class='top'></div>
	<div class='topright'></div>
	<div class='right'></div>
	<div class='left'></div>
	<div class='bottom'></div>
	<div class='bottomleft'></div>
	<div class='topleft'></div>
	<div class='bottomright'></div>
	<div class='leftcurvebox'></div>
	<div class='leftcurve'></div>
	<div class='leftcurve2'></div>
	<div class='rightcurvebox'></div>
	<div class='rightcurve'></div>
	<div class='rightcurve2'></div>
	<div class='circle1'></div>
	<div class='circle2'></div>
</div>
 

<style>
   body, html {
  background:black;
  margin: 0;
  height: 100%;
  width: 100%;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  background-size: 100%;
}

.wraper {
  height: 300px;
  width: 300px;
  background: transparent;
  border: 1px solid #178dee;
  border-radius: 100%;
  -webkit-box-shadow: 0px 0px 0px white,
 0px 0px 10px cyan,
 0px 0px 20px white,
 0px 0px 30px cyan,
 0px 0px 40px black,
 0px 0px 50px cyan,
 0px 0px 60px black;
          box-shadow: 0px 0px 0px white,
 0px 0px 10px cyan,
 0px 0px 20px white,
 0px 0px 30px cyan,
 0px 0px 40px black,
 0px 0px 50px cyan,
 0px 0px 60px black;
  -webkit-animation: ani 5s infinite;
          animation: ani 5s infinite;
}

@-webkit-keyframes ani {
  20% {
    border: 1px solid hotpink;
    -webkit-box-shadow: 0px 0px 0px white,
 0px 0px 10px hotpink,
 0px 0px 20px white,
 0px 0px 30px hotpink,
 0px 0px 40px black,
 0px 0px 50px hotpink,
 0px 0px 60px black;
            box-shadow: 0px 0px 0px white,
 0px 0px 10px hotpink,
 0px 0px 20px white,
 0px 0px 30px hotpink,
 0px 0px 40px black,
 0px 0px 50px hotpink,
 0px 0px 60px black;
  }
  40% {
    border: 1px solid #fabd21;
    -webkit-box-shadow: 0px 0px 0px white,
 0px 0px 10px #fabd21,
 0px 0px 20px white,
 0px 0px 30px #fabd21,
 0px 0px 40px black,
 0px 0px 50px #fabd21,
 0px 0px 60px black;
            box-shadow: 0px 0px 0px white,
 0px 0px 10px #fabd21,
 0px 0px 20px white,
 0px 0px 30px #fabd21,
 0px 0px 40px black,
 0px 0px 50px #fabd21,
 0px 0px 60px black;
  }
  60% {
    border: 1px solid red;
    -webkit-box-shadow: 0px 0px 0px white,
 0px 0px 10px red,
 0px 0px 20px white,
 0px 0px 30px red,
 0px 0px 40px white,
 0px 0px 50px red,
 0px 0px 60px black;
            box-shadow: 0px 0px 0px white,
 0px 0px 10px red,
 0px 0px 20px white,
 0px 0px 30px red,
 0px 0px 40px white,
 0px 0px 50px red,
 0px 0px 60px black;
  }
  80% {
    border: 1px solid #1bf013;
    -webkit-box-shadow: 0px 0px 0px white, 0px 0px 10px #1bf013, 0px 0px 20px white, 0px 0px 30px #1bf013, 0px 0px 40px black, 0px 0px 50px #1bf013, 0px 0px 60px black;
            box-shadow: 0px 0px 0px white, 0px 0px 10px #1bf013, 0px 0px 20px white, 0px 0px 30px #1bf013, 0px 0px 40px black, 0px 0px 50px #1bf013, 0px 0px 60px black;
  }
}

@keyframes ani {
  20% {
    border: 1px solid hotpink;
    -webkit-box-shadow: 0px 0px 0px white,
 0px 0px 10px hotpink,
 0px 0px 20px white,
 0px 0px 30px hotpink,
 0px 0px 40px black,
 0px 0px 50px hotpink,
 0px 0px 60px black;
            box-shadow: 0px 0px 0px white,
 0px 0px 10px hotpink,
 0px 0px 20px white,
 0px 0px 30px hotpink,
 0px 0px 40px black,
 0px 0px 50px hotpink,
 0px 0px 60px black;
  }
  40% {
    border: 1px solid #fabd21;
    -webkit-box-shadow: 0px 0px 0px white,
 0px 0px 10px #fabd21,
 0px 0px 20px white,
 0px 0px 30px #fabd21,
 0px 0px 40px black,
 0px 0px 50px #fabd21,
 0px 0px 60px black;
            box-shadow: 0px 0px 0px white,
 0px 0px 10px #fabd21,
 0px 0px 20px white,
 0px 0px 30px #fabd21,
 0px 0px 40px black,
 0px 0px 50px #fabd21,
 0px 0px 60px black;
  }
  60% {
    border: 1px solid red;
    -webkit-box-shadow: 0px 0px 0px white,
 0px 0px 10px red,
 0px 0px 20px white,
 0px 0px 30px red,
 0px 0px 40px white,
 0px 0px 50px red,
 0px 0px 60px black;
            box-shadow: 0px 0px 0px white,
 0px 0px 10px red,
 0px 0px 20px white,
 0px 0px 30px red,
 0px 0px 40px white,
 0px 0px 50px red,
 0px 0px 60px black;
  }
  80% {
    border: 1px solid #1bf013;
    -webkit-box-shadow: 0px 0px 0px white, 0px 0px 10px #1bf013, 0px 0px 20px white, 0px 0px 30px #1bf013, 0px 0px 40px black, 0px 0px 50px #1bf013, 0px 0px 60px black;
            box-shadow: 0px 0px 0px white, 0px 0px 10px #1bf013, 0px 0px 20px white, 0px 0px 30px #1bf013, 0px 0px 40px black, 0px 0px 50px #1bf013, 0px 0px 60px black;
  }
}

@-webkit-keyframes nani {
  20% {
    background: hotpink;
  }
  40% {
    background: #fabd21;
  }
  60% {
    background: rgb(253, 11, 11);
  }
  80% {
    background: #1bf013;
  }
}

@keyframes nani {
  20% {
    background: hotpink;
  }
  40% {
    background: #fabd21;
  }
  60% {
    background: rgb(253, 11, 11);
  }
  80% {
    background: #1bf013;
  }
}

.str {
  height: 100px;
  width: 100px;
  position: absolute;
  margin-top: 100px;
  margin-left: 100px;
  brdr: 1px white solid;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
}

.top {
  height: 42px;
  width: 100px;
  position: absolute;
  margin-left: 100px;
  margin-top: 48px;
  border-top-left-radius: 30px;
  border-top-right-radius: 30px;
  brdr: 1px white solid;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  background: #178dee;
  -webkit-animation: nani 5s infinite;
          animation: nani 5s infinite;
}

.right {
  height: 100px;
  width: 42px;
  position: absolute;
  margin-left: 208px;
  margin-top: 100px;
  border-top-right-radius: 30px;
  border-bottom-right-radius: 30px;
  brdr: 1px white solid;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  -webkit-animation: nani 5s infinite;
          animation: nani 5s infinite;
  background: #178dee;
}

.left {
  height: 100px;
  width: 42px;
  position: absolute;
  margin-left: 50px;
  margin-top: 100px;
  border-top-left-radius: 30px;
  border-bottom-left-radius: 30px;
  brdr: 1px white solid;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  -webkit-animation: nani 5s infinite;
          animation: nani 5s infinite;
  background: #178dee;
}

.bottom {
  height: 42px;
  width: 100px;
  position: absolute;
  margin-left: 100px;
  margin-top: 210px;
  border-bottom-left-radius: 30px;
  border-bottom-right-radius: 30px;
  brdr: 1px white solid;
  -webkit-animation: nani 5s infinite;
          animation: nani 5s infinite;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  background: #178dee;
}

.topright {
  height: 55px;
  width: 50px;
  position: absolute;
  margin-left: 150px;
  margin-top: 90px;
  border-bottom-right-radius: 30px;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  background: #178dee;
  -webkit-animation: nani 5s infinite;
          animation: nani 5s infinite;
  brdr: 1px red solid;
  z-index: 3;
}

.bottomleft {
  height: 55px;
  width: 50px;
  position: absolute;
  margin-left: 100px;
  margin-top: 155px;
  border-top-left-radius: 30px;
  brdr: 1px red solid;
  -webkit-animation: nani 5s infinite;
          animation: nani 5s infinite;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  background: #178dee;
  z-index: 3;
}

.topleft {
  height: 44.5px;
  width: 70px;
  position: absolute;
  margin-left: 90px;
  margin-top: 100px;
  brdr: 1px blue solid;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  -webkit-animation: nani 5s infinite;
          animation: nani 5s infinite;
  background: #178dee;
}

.bottomright {
  height: 44.5px;
  width: 70px;
  position: absolute;
  margin-left: 145px;
  margin-top: 155px;
  brdr: 1px blue solid;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  -webkit-animation: nani 5s infinite;
          animation: nani 5s infinite;
  background: #178dee;
}

.leftcurvebox {
  height: 32px;
  width: 32px;
  position: absolute;
  margin-left: 92px;
  margin-top: 144px;
  brdr: 1px green solid;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  -webkit-animation: nani 5s infinite;
          animation: nani 5s infinite;
  background: #178dee;
}

.leftcurve {
  height: 32px;
  width: 32px;
  position: absolute;
  margin-left: 92px;
  margin-top: 144px;
  brdr: 1px green solid;
  border-top-left-radius: 100%;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  background: black;
}

.rightcurvebox {
  height: 32px;
  width: 32px;
  position: absolute;
  margin-left: 176px;
  margin-top: 124px;
  brdr: 1px green solid;
  -webkit-animation: nani 5s infinite;
          animation: nani 5s infinite;
  background: #178dee;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
}

.rightcurve {
  height: 32px;
  width: 32px;
  position: absolute;
  margin-left: 176px;
  margin-top: 124px;
  brdr: 1px green solid;
  border-bottom-right-radius: 100%;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  background: black;
}

.circle1 {
  height: 17px;
  width: 17px;
  background-color: black;
  border-radius: 100%;
  margin-top: 65px;
  margin-left: 115px;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  position: absolute;
}

.circle2 {
  position: absolute;
  height: 17px;
  width: 17px;
  background-color: black;
  border-radius: 100%;
  margin-top: 220px;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  margin-left: 170px;
  z-index: 2;
}

.django {
color: blue;
}

</style>
