// Copyright (c) 2023, Peter Maged
// For license information, please see license.txt

frappe.ui.form.on('Employee Checkin', {
  onload: (frm) => {
    if (frm.is_new()) {
      getAndSetCurrentLocation(frm);

      getLocalIPAddress()
        .then(ipAddress => {
          console.log('Local IP Address:', ipAddress)
          frm.set_value("ip" , ipAddress)    
          
          frappe.call({
                    method: "overrides.employee_checkin.GPSEmployeeCheckin.get_mac",
                    args: { ip_address: ipAddress },
                    callback: function(response) {
                        if (response.message) {
                            console.log('MAC Address:', response.message);
                        } else {
                            console.error('No MAC Address found');
                        }
                    },
                    error: function(error) {
                        console.error('Error calling get_mac:', error);
                    }
                });
        })
        .catch(error => console.error('Error getting local IP address:', error));
      
    }
  },
  employee_location(frm) {
    let latitude = '';
    let longitude = '';
    let location_field = JSON.parse(frm.doc.employee_location);
    if (
      location_field &&
      location_field.features &&
      location_field.features.length > 0
    ) {
      let cur_location = location_field.features[0].geometry.coordinates;
      latitude = cur_location[1];
      longitude = cur_location[0];
    }
    frm.set_value('latitude', latitude);
    frm.set_value('longitude', longitude);
  },
});

function getAndSetCurrentLocation(frm) {
  // Check if the Geolocation API is supported
  if (navigator.geolocation) {
    // Get the current position
    navigator.geolocation.getCurrentPosition(
      function (position) {
        // Set the latitude and longitude values in the Geolocation field
        let latitude = position.coords.latitude;
        let longitude = position.coords.longitude;
        let cur_location = {
          type: 'FeatureCollection',
          features: [
            {
              type: 'Feature',
              properties: {},
              geometry: { type: 'Point', coordinates: [longitude, latitude] },
            },
          ],
        };
        frm.set_value('employee_location', JSON.stringify(cur_location));
        frm.refresh_field('employee_location');
        frappe.msgprint(__('Location updated successfully.'));
      },
      function (error) {
        // Handle errors
        console.error('Error getting location:', error);
        frappe.msgprint(__('Error getting location. Please try again.'));
      },
    );
  } else {
    frappe.msgprint(__('Geolocation is not supported in this browser.'));
  }
}




function getLocalIPAddress() {
  return new Promise((resolve, reject) => {
    const rtcConfig = { iceServers: [{ urls: 'stun:stun.l.google.com:19302' }] };
    const rtcPeerConnection = new RTCPeerConnection(rtcConfig);

    rtcPeerConnection.createDataChannel('');

    rtcPeerConnection.createOffer()
      .then(offer => rtcPeerConnection.setLocalDescription(offer))
      .catch(error => reject(error));

    rtcPeerConnection.onicecandidate = (event) => {
      if (event.candidate) {
        const ipRegex = /\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/;
        const ipAddress = ipRegex.exec(event.candidate.candidate)[0];
        resolve(ipAddress);
        rtcPeerConnection.onicecandidate = null; // Cleanup
      }
    };
  });
}
