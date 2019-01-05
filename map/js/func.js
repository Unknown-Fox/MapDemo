alert("fuck");
function AddMarker(x,y,name)
{
  var myIcon = new BMap.Icon("images/PointBlue.png", new BMap.Size(20,25));
  var x_ = parseInt(x);
  var y_ = parseInt(y);
  pixel = new BMap.Pixel(x_,y_);
  var point = map.pixelToPoint(pixel);
  // map.centerAndZoom(point, 15);
  var marker = new BMap.Marker(point,{icon:myIcon});        // 创建标注
  marker.enableDragging();
  label= new BMap.Label(name)
  size1= new BMap.Size(0, -15);
  size2= new BMap.Size(0, -30);
  marker.setOffset(size1);
  label.setOffset(size2);
  label.setStyle({ color : "blue" });
  marker.setLabel(label)
  map.addOverlay(marker);
}