import Ember from 'ember';

export default Ember.View.extend({
  templateName: 'dashboard',
  didInsertElement: function() {
    console.log("Did insert dashboard.");
    //this._super();

    /*$('#datasetSelect').selectpicker();*/

  }
});
