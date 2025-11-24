"""
AI Deep Learning Platform - Flask Application
Main app file for PythonAnywhere
"""

from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'

# ============================================================================
# ROUTES
# ============================================================================

@app.route('/')
def index():
    """Login page"""
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    """Student dashboard (protected - requires Firebase auth)"""
    return render_template('dashboard.html')


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'message': 'AI Deep Learning API is running'
    })


@app.route('/api/user/profile', methods=['GET'])
def get_user_profile():
    """
    Get user profile from Firebase token
    TODO: Verify Firebase token and return user data from PostgreSQL
    """
    # This will be implemented after Django backend setup
    return jsonify({
        'status': 'error',
        'message': 'Not implemented yet'
    }), 501


@app.route('/api/user/progress', methods=['GET'])
def get_user_progress():
    """
    Get user progress/learning data
    TODO: Query PostgreSQL for student progress
    """
    return jsonify({
        'status': 'error',
        'message': 'Not implemented yet'
    }), 501


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Page not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Internal server error'
    }), 500


# ============================================================================
# DEVELOPMENT
# ============================================================================

if __name__ == '__main__':
    # For local testing only
    # PythonAnywhere will run this via WSGI
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )
