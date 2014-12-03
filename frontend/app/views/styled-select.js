import Ember from 'ember';

export default Ember.Select.extend({
  didInsertElement: function() {
    this._super();

    console.log("Selection element inserted.");
    ///Ember.$('.styled-select').selectpicker();
  }
});
