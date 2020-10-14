from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

DEVELOPERS = {
    1: "sai",
    2: "akhil",
    3: "kolla"
}

TASKS = {
    1: "Develop an API", 2: "Unit testing",
    3: "Design the database", 4: "Normalize the database",
    5: "Deploy to cloud", 6: "Integrated testing",

}

DEVELOPER_TASKS = {
    DEVELOPERS[1]: [TASKS[1], TASKS[2]],
    DEVELOPERS[2]: [TASKS[3], TASKS[5]],
    DEVELOPERS[3]: [TASKS[6], TASKS[4]]
}
parser = reqparse.RequestParser()
parser.add_argument('1')

parsers = reqparse.RequestParser()
parsers.add_argument('1')

parsered = reqparse.RequestParser()
parsered.add_argument('task1')

def abort_if_dev_doesnt_exist(developers_id):
    if developers_id not in DEVELOPERS:
        abort(404, message="developer {} doesn't exist".format(developers_id))

def abort_if_task_doesnt_exist(task_id):
    if task_id not in TASKS:
        abort(404, message="Todo {} doesn't exist".format(task_id))

def abort_if_dev_tasks_doesnt_exist(devtask_id):
    if devtask_id not in DEVELOPERS:
        abort(404, message="Todo {} doesn't exist".format(devtask_id))


class Developer(Resource):
    def get(self,developers_id):
        abort_if_dev_doesnt_exist(developers_id)
        return DEVELOPERS[developers_id]

    def delete(self, developers_id):
        abort_if_dev_doesnt_exist(developers_id)
        del DEVELOPERS[developers_id]
        return '', 204

    def post(self, developers_id):
        args = parser.parse_args()
        name = {developers_id : args['1']}
        DEVELOPERS[developers_id] = name
        return name, 201

class Tasks(Resource):
    def get(self,task_id):
        abort_if_task_doesnt_exist(task_id)
        return TASKS[task_id]

    def delete(self, task_id):
        abort_if_task_doesnt_exist(task_id)
        del TASKS[task_id]
        return '', 204

    def post(self, task_id):
        args = parsers.parse_args()
        name = {task_id: args['1']}
        TASKS[task_id] = name
        return name, 201

class Developer_Tasks(Resource):
    def get(self,devtask_id):
        abort_if_dev_tasks_doesnt_exist(devtask_id)
        return DEVELOPER_TASKS[DEVELOPERS[devtask_id]]

    def delete(self, devtask_id):
        abort_if_dev_tasks_doesnt_exist(devtask_id)
        del DEVELOPER_TASKS[devtask_id]
        return '', 204
    
    def post(self, devtask_id):
        args = parsered.parse_args()
        name = {DEVELOPERS[devtask_id]: args['task1']}
        DEVELOPER_TASKS[DEVELOPERS[devtask_id]] = name
        return name, 201

class DeveloperList(Resource):
    def get(self):
        return DEVELOPERS
    
    def post(self):
        args = parser.parse_args()
        developers_id = int(max(DEVELOPERS.keys())) + 1
        DEVELOPERS[developers_id] = {developers_id : args['1']}
        return DEVELOPERS[developers_id], 201

class TaskList(Resource):
    def get(self):
        return TASKS
    
    def post(self):
        args = parser.parse_args()
        task_id = int(max(DEVELOPERS.keys())) + 1
        DEVELOPERS[task_id] = {task_id : args['1']}
        return DEVELOPERS[task_id], 201

class DeveloperTaskList(Resource):
    def get(self):
        return DEVELOPER_TASKS


api.add_resource(Developer, '/developer/<int:developers_id>')
api.add_resource(Tasks, '/task/<int:task_id>')

api.add_resource(Developer_Tasks, '/devtask/<int:devtask_id>/task')


api.add_resource(DeveloperList, '/developer')

api.add_resource(TaskList, '/task')

api.add_resource(DeveloperTaskList, '/developer/task')


if __name__ == '__main__':
    app.run(port = 5000 , debug = True )