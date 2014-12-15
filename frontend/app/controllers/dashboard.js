import Ember from 'ember';

export default Ember.Controller.extend({
  datafiles: Ember.computed.mapBy('datasets', 'names'),
  classifier_files: Ember.computed.mapBy('classifiers', 'names'),
  selectedDatasets: [],
  selectedClassifiers: [],
  selectedOutput: null,
  emptyDatasets: function() {
    var sel_datasets = this.get('selectedDatasets');
    var sel_classifiers = this.get('selectedClassifiers');
    console.log("Empty datasets!");
    console.log(sel_datasets.length);
    console.log(sel_classifiers.length);

    return (sel_datasets.length === 0 || sel_classifiers.length === 0);
  }.property('selectedDatasets', 'selectedClassifiers'),
  actions: {
    submit: function() {
      //alert("Form submitted with the following files!");
      //alert(this.get('selectedDatasets'));
      console.log(this.get('selectedDatasets'));

      var selected_file = this.get('selectedDatasets');
      var selected_classifiers = this.get('selectedClassifiers');
      console.log(selected_classifiers);
      console.log(selected_file);

      var analysis = this.store.createRecord('analysis', {
        'title': "Testing",
        'classifier_ids': selected_classifiers,
      });

      //analysis.save();

      this.store.find('dataset', selected_file).then(function(file) {
        console.log("Analysis set.");
        analysis.set('dataset', file);
        analysis.save();
      });


      /*for(var i = 0; i < selected_classifiers.length; i++) {
        var item = this.store.find('classifier', selected_classifiers[i]).then(function(classifier) {

          console.log(classifier);
          analysis.get("classifiers").then(function(classifiers) {
            console.log("After getting.");
            console.log(classifier);
            classifiers.pushObject(classifier);
            //analysis.save();
            console.log("Item pushed!");
          });
        });
      }*/

  },

  selectOutput: function(output) {
    this.set('selectedOutput', output);
    console.log(output);
  }
 }
});