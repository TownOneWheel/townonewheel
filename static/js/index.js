// 1. 지도 div 취득 및 옵션 설정
const container = document.getElementById('map');
const options = {
  center: new kakao.maps.LatLng(37.547076399306, 127.04020267241),
  level: 3,
};

// 마커 이미지 커스텀
const imageSrc = 'https://img.icons8.com/ios-glyphs/60/000000/pet-commands-summon.png',
  imageSize = new kakao.maps.Size(30, 30), // 마커이미지의 크기입니다
  imageOption = { offset: new kakao.maps.Point(15, 30) },
  markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption);

// 2. api로 지도 생성하여 map 변수에 할당
const map = new kakao.maps.Map(container, options);
// 3. 마커를 위치시킬 포지션을 position 변수에 할당 (서울숲 위/경도 또는 사용자 위치 받아와서 할당)
const position = new kakao.maps.LatLng(37.547076399306, 127.04020267241);
// 4. 할당한 position정보를 담아 marker 변수에 마커 객체 생성
let marker = new kakao.maps.Marker({
  map: map, // 5번과 중복되는 역할인듯?
  position: position, //10-1. 마커를 특정 위치가 아니라 지도 중심좌표에 위치시키려면 map.getCenter()
  clickable: true, // 8-2. 지도에 클릭이벤트가 아니라 마커에 클릭이벤트를 발생시킨다.
  image: markerImage,
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

if (navigator.geolocation) {
  // GeoLocation을 이용해서 접속 위치를 얻어옵니다
  navigator.geolocation.getCurrentPosition(function (position) {
    const lat = position.coords.latitude, // 위도
      lon = position.coords.longitude; // 경도

    const locPosition = new kakao.maps.LatLng(lat, lon), // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
      message = '<div style="padding:5px;">사용자가 있는 위치</div>'; // 인포윈도우에 표시될 내용입니다

    // 마커와 인포윈도우를 표시합니다
    displayMarker(locPosition, message);
  });
} else {
  // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다

  const locPosition = new kakao.maps.LatLng(37.547076399306, 127.04020267241),
    message = 'geolocation을 사용할수 없어요..';

  displayMarker(locPosition, message);
}

// 지도에 마커와 인포윈도우를 표시하는 함수
function displayMarker(locPosition, message) {
  // 마커를 생성합니다
  const marker = new kakao.maps.Marker({
    map: map,
    position: locPosition,
  });

  const iwContent = message, // 인포윈도우에 표시할 내용
    iwRemoveable = true;

  // 인포윈도우를 생성합니다
  const infowindow = new kakao.maps.InfoWindow({
    content: iwContent,
    removable: iwRemoveable,
  });

  // 인포윈도우를 마커위에 표시합니다
  infowindow.open(map, marker);

  // 지도 중심좌표를 접속위치로 변경합니다
  map.setCenter(locPosition);
}
