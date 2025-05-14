frappe.ui.form.on('Branch', {
  onload: (frm) => {
    if (frm.is_new()) {
      getAndSetCurrentLocation(frm);
    }
  },
  branch_location(frm) {
    let latitude = '';
    let longitude = '';
    let location_field = JSON.parse(frm.doc.branch_location);
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
        let cur_location = {"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[longitude,latitude]}}]};
        frm.set_value('branch_location', JSON.stringify(cur_location));
        frm.refresh_field('branch_location');
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
