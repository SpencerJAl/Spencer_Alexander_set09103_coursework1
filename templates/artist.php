<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, inital-scale=1">
<link href="{{url_for('static',filename='bootstrap-3.3.5-dist/css/bootstrap.min.css')}}" rel="stylesheet"/>
<link href="{{url_for('static',filename='style.css')}}" rel="stylesheet"/>
<script src="{{ url_for('static',filename='bootstrap-3.3.5-dist/js/bootstrap.min.js')}}"></script>
<script src="{{ url_for('static',filename='cw1.js')}}"></script>
<script>

</script>
<title>Artists</title>
</head>
<body>
<div id="artisthead">
<h1>Artist's</h1
</div>
<p>Through out the history of our work there have been many artist, please
feel free to look through the following list and learn a small bit about them,
or enter their names into the search bar to learn more about them or view some of their
paintings</p>
<form method="post" action="add.php">
<p>Enter Artist name to learn more:<input type="text" name="painter"
id="painter"><input type="submit" name="name" id="search" value="Search
Painter" class="btn btn-success"></p>
</form>
<div id="painter">

 <div class="col-md-4">
  <div class="thumbnail">
   <img src="{{ url_for('static', filename='pablo.jpg')}}" alt="A Photograph of
   famous artist pablo picasso"/>
   <div class="caption">
    <p>Pablo Picasso is a famous 19th & 20th century painter from Spain. He is
    most famous for his orignal paintgs based on the style we now call
    cubism</p>
   </div>
  </div>
 </div>

 <div class="col-md-4">
  <div class="thumbnail">
   <img src="{{ url_for('static', filename='leonardo.jpg')}}" alt="A painting
   of famous artist leonardo da vinci"/>
   <div class="caption">
    <p>Leonardo Da Vinci, is without a doubt one of the most famous painters of
    all time. Oringally from Italy, Leonardo is most famous for his painting
    "The mona lisa"</p>
    </div>
   </div>
  </div>

  <div class="col-md-4">
   <div class="thumbnail">
    <img src="{{ url_for('static', filename='vincent.jpg')}}" alt="A painting
    of vincent van gogh"/>
     <div class="caption">
      <p>Vincent Van Gogh, also known as "The mad painter", is a famous painter
      known for his unqiue art style, which while at the time was critized, has
      since become a world wide phenomenon</p>
     </div>
    </div>
   </div>
</div>
</body>
</html>
