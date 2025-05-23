# UTEC Faculty Network Visualization

This project visualizes the relationships between UTEC professors and their departments/research groups as a network graph. The visualization uses D3.js for interactive data exploration within a Flask web application.

## Research Questions

This network visualization was designed to answer the following key questions:

1. **Which professors act as bridges between multiple research groups/departments?**
   - Identifies professors who serve as connectors between different academic units
   - Highlights potential interdisciplinary collaboration opportunities
   - Shows the diversity of research interests among faculty

2. **How interconnected are different research departments through shared faculty?**
   - Reveals the strength of connections between different academic units
   - Identifies department pairs with the most collaboration potential
   - Shows the overall structure of interdepartmental relationships

3. **Which research groups have the most professors, and does this correlate with their connectivity?**
   - Examines whether larger departments/groups have more connections
   - Identifies which departments may serve as central hubs in the network
   - Provides insights into resource distribution across the university

4. **Are there isolated clusters of researchers that have no connections to other departments?**
   - Identifies potential silos within the academic structure
   - Highlights opportunities for new collaborative initiatives
   - Shows the overall cohesiveness of the university's research network

## Development Process

### Data Processing
1. Parsed the CSV data of UTEC professors
2. Created two types of nodes: professors and organizations (departments/research groups)
3. Established connections (edges) between professors and their affiliated organizations
4. Generated JSON files for network visualization

### Visualization Design
1. Used D3.js force-directed graph layout to visualize the network
2. Applied different colors to distinguish between professors and organizations
3. Sized nodes based on their connectivity to highlight important entities
4. Implemented interactive features:
   - Hover tooltips with additional information
   - Click highlighting to focus on specific connections
   - Filters to explore departments and bridge professors
   - Zoom and pan for easier navigation

### Analysis Features
1. Automatically identifies and lists "bridge professors" with multiple affiliations
2. Calculates and displays interdepartmental connectivity metrics
3. Provides network statistics for high-level insights
4. Allows filtering by department to explore specific relationships

## How to Run

1. Make sure you have Python installed with Flask
2. Install the required dependencies:
   ```
   pip install flask
   ```
3. Run the Flask application:
   ```
   python app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:5000/`

## Project Structure

- `app.py` - Flask application
- `templates/index.html` - Main HTML template with D3.js visualization
- `static/css/style.css` - Styling for the visualization
- `static/data/` - Directory for generated JSON data files
- `utec_people.csv` - Original data source



## Student: Camila Rodriguez Valverde