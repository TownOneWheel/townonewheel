// 1. 지도 div 취득 및 옵션 설정
const container = document.getElementById('map');
const options = {
  center: new kakao.maps.LatLng(37.547076399306, 127.04020267241),
  level: 3,
};

// 2. api로 지도 생성하여 map 변수에 할당
const map = new kakao.maps.Map(container, options);
// 3. 마커를 위치시킬 포지션을 position 변수에 할당 (서울숲 위/경도 또는 사용자 위치 받아와서 할당)
const position = new kakao.maps.LatLng(37.547076399306, 127.04020267241);
// 4. 할당한 position정보를 담아 marker 변수에 마커 객체 생성
let marker = new kakao.maps.Marker({
  map: map, // 5번과 중복되는 역할인듯?
  position: position, //10-1. 마커를 특정 위치가 아니라 지도 중심좌표에 위치시키려면 map.getCenter()
  clickable: true, // 8-2. 지도에 클릭이벤트가 아니라 마커에 클릭이벤트를 발생시킨다.
});
// 5. 4에서 생성한 마커 객체 marker을 2에서 생성한 지도 객체 위에 세팅 (이 map을 세팅하는 위치가 중요할듯)
marker.setMap(map);

// 6. 인포윈도우 태그 만들어 할당 (7은 마우스오버로 띄우기, 8은 클릭으로 창 여닫기)
const infoWindowContent =
  '<div class="info_window" style="padding:5px;">고양이 정보가 나타나는 곳</div>';
// 7-1. 8-1. 인포윈도우 객체를 생성하여 infowindow 변수에 할당
const infowindow = new kakao.maps.InfoWindow({
  content: infoWindowContent,
  removable: true, // 8-3. 인포윈도우를 닫을 수 있는 x버튼 표시 옵션
});
// 7-2. 4에서 생성한 마커 객체에 마우스오버와 마우스아웃 이벤트핸들러 open/close(api 메서드) 등록
kakao.maps.event.addListener(marker, 'mouseover', function () {
  infowindow.open(map, marker);
});
kakao.maps.event.addListener(marker, 'mouseout', function () {
  infowindow.close();
});
// 8-2. 마커에 클릭이벤트를 발생시키기 위해 4번에 마커 객체를 생성하면서 clickable 옵션을 준다.
// 8-3. 인포윈도우를 닫는 버튼을 생성하는 removable 옵션을 준다.
// 8-4. 4에서 생성한 마커 객체의 클릭이벤트에 open/close 메서드를 등록한다.
// kakao.maps.event.addListener(marker, 'click', function() {
//   infowindow.open(map, marker);  // 마커 위에 인포윈도우를 표시합니다
// });

// // 9. 마커이미지 만들기
// const imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_red.png', // 마커이미지 주소
// imageSize = new kakao.maps.Size(64, 69), // 마커이미지의 크기
// imageOption = {offset: new kakao.maps.Point(27, 69)}; // 이미지 안에서의 마커의 좌표를 설정.

// const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption),
// markerPosition = new kakao.maps.LatLng(37.54699, 127.09598);

// // 10. 클릭한 위치에 마커 표시하는 법 : 4에서 마커 객체 생성할 때의 포지션을 map.getCenter()로 마커를 생성해둔다.
// // 10-2. 지도에 클릭이벤트를 발생시킨다.
// kakao.maps.event.addListener(map, 'click', function(mouseEvent) {

// // 10-3. 클릭한 위도, 경도 정보 취득
// const latlng = mouseEvent.latLng;

// // 10-4. 마커 위치를 클릭한 위치로 이동
// marker.setPosition(latlng);

// // 10-5. 마커 위치에 대해 정보를 가져와 텍스트로 출력하는 것 (우리는 필요없을듯)
// let message = '클릭한 위치의 위도는 ' + latlng.getLat() + ' 이고, ';
// message += '경도는 ' + latlng.getLng() + ' 입니다';

// const resultDiv = document.getElementById('clickLatlng');
// resultDiv.innerHTML = message;
// });