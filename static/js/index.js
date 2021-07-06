const $mapContainer = document.getElementById('map'); //지도 div element 취득
const markerImageSrc = 'https://img.icons8.com/ios-glyphs/60/000000/cat.png',
  markerImageSize = new kakao.maps.Size(40, 40),
  markerImagePosition = { offset: new kakao.maps.Point(27, 40) };

if (navigator.geolocation) {
  console.log('lalalalal');
  // GeoLocation가 활성화되어있는 경우 접속 위치 취득 및 콜백함수 호출
  navigator.geolocation.getCurrentPosition(function (position) {
    const lat = position.coords.latitude, // 위도 취득
      lon = position.coords.longitude; // 경도 취득
    console.log(lat, lon);

    const mapOption = {
      center: new kakao.maps.LatLng(lat, lon), // 지도의 중심좌표
      level: 3, // 지도의 확대 레벨
    };
    const map = new kakao.maps.Map($mapContainer, mapOption); // 지도 생성 및 할당

    // 마커 생성
    const markerPosition = new kakao.maps.LatLng(lat, lon); // geolocation으로 취득한 위치에 마커 생성

    const marker = new kakao.maps.Marker({
      map: map,
      draggable: true,
      clickable: true,
      position: markerPosition,
      image: new kakao.maps.MarkerImage(markerImageSrc, markerImageSize, markerImagePosition),
    }); //마커 생성 및 할당

    // 인포윈도우 생성
    const infowindow = new kakao.maps.InfoWindow({
      content: `<div class="cat-register" style="padding:5px;">
      <form method="POST" action=""><input type="text" name="position" value="${lat}"/>이곳에 고양이를 <button type="submit">등록</button></form></div>`,
      removable: true, //닫기 버튼 활성화
    });

    // 인포윈도우를 마커위에 표시
    infowindow.open(map, marker);

    // 클릭한 위치에 마커 생성
    kakao.maps.event.addListener(map, 'click', function (mouseEvent) {
      // 클릭한 위도, 경도 정보를 가져옵니다
      const latlng = mouseEvent.latLng;

      // 마커 위치를 클릭한 위치로 옮깁니다
      marker.setPosition(latlng);
      infowindow.setContent(`${latlng.getLat()}, ${latlng.getLng()}`);
      infowindow.open(map, marker);
      console.log(latlng.getLat(), latlng.getLng());
    });
  });
} else {
  console.log('lalala');
  const mapOption = {
    center: new kakao.maps.LatLng(37.547076399306, 127.04020267241), // 지도의 중심좌표
    level: 10, // 지도의 확대 레벨
  };
  const map = new kakao.maps.Map($mapContainer, mapOption); // 지도를 생성합니다

  const marker = new kakao.maps.Marker({
    map: map,
    draggable: true,
    clickable: true,
    position: new kakao.maps.LatLng(37.547076399306, 127.04020267241),
    image: new kakao.maps.MarkerImage(
      'https://img.icons8.com/ios-glyphs/60/000000/cat.png',
      new kakao.maps.Size(40, 40),
      { offset: new kakao.maps.Point(27, 40) }
    ),
  }); //마커 생성 및 할당

  // 인포윈도우 생성
  const infowindow = new kakao.maps.InfoWindow({
    content: '<div style="padding:5px;">고양이가 이곳에 있나요?</div>',
    removable: true, //닫기 버튼 활성화
  });

  // 인포윈도우를 마커위에 표시
  infowindow.open(map, marker);

  kakao.maps.event.addListener(map, 'click', function (mouseEvent) {
    // 클릭한 위도, 경도 정보를 가져옵니다
    const latlng = mouseEvent.latLng;

    // 마커 위치를 클릭한 위치로 옮깁니다
    marker.setPosition(latlng);
    infowindow.open(map, marker);
    console.log(latlng.getLat(), latlng.getLng());
  });
}
// var positions = [
//   {
//     title: '카카오',
//     latlng: new kakao.maps.LatLng(33.450705, 126.570677),
//   },
//   {
//     title: '생태연못',
//     latlng: new kakao.maps.LatLng(33.450936, 126.569477),
//   },
//   {
//     title: '텃밭',
//     latlng: new kakao.maps.LatLng(33.450879, 126.56994),
//   },
//   {
//     title: '근린공원',
//     latlng: new kakao.maps.LatLng(33.451393, 126.570738),
//   },
// ];

// 마커 이미지의 이미지 주소입니다

// for (var i = 0; i < positions.length; i++) {
//   // 마커 이미지의 이미지 크기 입니다
//   var imageSize = new kakao.maps.Size(24, 35);

//   // 마커 이미지를 생성합니다
//   var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

//   // 마커를 생성합니다
//   var marker = new kakao.maps.Marker({
//     map: map, // 마커를 표시할 지도
//     position: positions[i].latlng, // 마커를 표시할 위치
//     title: positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
//     image: markerImage, // 마커 이미지
//   });
// }
