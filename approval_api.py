from flask import Flask, jsonify, request
from uuid import uuid4
from threading import Lock

app = Flask(__name__)

# In-memory store for pending approvals
pending_approvals = {}
approval_lock = Lock()

@app.route('/approvals', methods=['GET'])
def list_approvals():
    with approval_lock:
        return jsonify(list(pending_approvals.values()))

@app.route('/approvals', methods=['POST'])
def create_approval():
    data = request.json
    approval_id = str(uuid4())
    approval = {
        'id': approval_id,
        'status': 'pending',
        'suggestion': data.get('suggestion'),
        'error': data.get('error'),
        'details': data.get('details', {})
    }
    with approval_lock:
        pending_approvals[approval_id] = approval
    return jsonify(approval), 201

@app.route('/approvals/<approval_id>/approve', methods=['POST'])
def approve_action(approval_id):
    with approval_lock:
        approval = pending_approvals.get(approval_id)
        if not approval:
            return jsonify({'error': 'Not found'}), 404
        approval['status'] = 'approved'
    return jsonify(approval)

@app.route('/approvals/<approval_id>/reject', methods=['POST'])
def reject_action(approval_id):
    with approval_lock:
        approval = pending_approvals.get(approval_id)
        if not approval:
            return jsonify({'error': 'Not found'}), 404
        approval['status'] = 'rejected'
    return jsonify(approval)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
