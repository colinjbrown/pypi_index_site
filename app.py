from flask import Flask, render_template, request, url_for, redirect
import pymongo
from wtforms import Form, SelectField, StringField, validators

class SearchForm(Form):
    query_val = StringField('Search',[validators.Length(min=1)])
    query = SelectField(u'Query Type', choices=[('module', 'Module/Submodule'), ('version', 'Versions'), ('psubs', 'Package Submodules'),('meta','Database Metadata')])

client = pymongo.MongoClient("mongodb://public1:public1@23.234.231.89:12438/pypi_mod_index",serverSelectionTimeoutMS=5000)
client.server_info()
mongo_flag = True
db = client["pypi_mod_index"]
top = db['modules']
subs = db['submodules']
v_client = pymongo.MongoClient("mongodb://public1:public1@23.234.231.89:12438/pypi3",serverSelectionTimeoutMS=5000)
v_db = v_client["pypi3"]
metadata = v_db['metadata']
versions = v_db['versions']

app = Flask(__name__)
function_map = {'version':'get_versions','psubs':'get_submodules','meta':'get_metadata'}


@app.route('/',methods=['GET','POST'])
def search():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        if form.query.data == 'module':
            mod_split = form.query_val.data.split('.')
            if len(mod_split) == 1:
                return redirect(url_for('get_modules',module=form.query_val.data))
            else:
                return redirect(url_for('get_modules',module=mod_split[0],submodule=mod_split[1]))
        else:
            #This should never happen but you can probably post with bad values
            if form.query.data in function_map:
                function = function_map[form.query.data]
                return redirect(url_for(function,package=form.query_val.data))
    return render_template('search.html',form=form)

@app.route('/modules/<module>')
@app.route('/modules/<module>/<submodule>')
def get_modules(module,submodule=None):
    if submodule:
        return str(list(subs.find({'submodule':module+'.'+submodule})))
    else:
        return str(list(top.find({'module':module})))

@app.route('/metadata/<package>')
def get_metadata(package):
    return str(list(metadata.find({'package': package})))

@app.route('/versions/<package>')
def get_versions(package):
    return str(list(versions.find({'package': package})))

@app.route('/psubs/<package>')
def get_submodules(package):
    return str(list(subs.aggregate([{'$match':{'packages.package':package}},{'$unwind':'$packages'},{'$group':{'_id':'$packages.package','submodules':{'$addToSet':'$submodule'}}}])))#,{'$unwind':'$versions'}


if __name__ == '__main__':
    app.run()
