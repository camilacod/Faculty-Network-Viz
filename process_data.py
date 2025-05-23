import csv
import json

def process_data():
    nodes = []
    edges = []
    
    # Node types
    PERSON = 'person'
    ORGANIZATION = 'organization'
    
    # Track existing nodes to avoid duplicates
    existing_nodes = {}
    node_id_counter = 0
    
    with open('utec_people.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            person_id = node_id_counter
            node_id_counter += 1
            
            # Add person node
            person_node = {
                'id': person_id,
                'name': row['nombre'],
                'type': PERSON,
                'email': row['email'],
                'url': row['url_perfil'],
                'image': row['imagen_url']
            }
            nodes.append(person_node)
            existing_nodes[row['nombre']] = person_id
            
            # Process organizations (departments/research groups)
            if row['organizaciones']:
                orgs = row['organizaciones'].split(';')
                for org in orgs:
                    parts = org.split('-')
                    if len(parts) >= 1:
                        org_name = parts[0].strip()
                        
                        # Create organization node if it doesn't exist
                        if org_name not in existing_nodes:
                            org_id = node_id_counter
                            node_id_counter += 1
                            
                            org_node = {
                                'id': org_id,
                                'name': org_name,
                                'type': ORGANIZATION
                            }
                            nodes.append(org_node)
                            existing_nodes[org_name] = org_id
                        else:
                            org_id = existing_nodes[org_name]
                        
                        # Create edge between person and organization
                        edges.append({
                            'source': person_id,
                            'target': org_id,
                            'relationship': parts[1].strip() if len(parts) > 1 else 'Miembro'
                        })
    
    # Save to JSON files
    with open('static/data/nodes.json', 'w', encoding='utf-8') as f:
        json.dump(nodes, f, ensure_ascii=False, indent=2)
    
    with open('static/data/edges.json', 'w', encoding='utf-8') as f:
        json.dump(edges, f, ensure_ascii=False, indent=2)
    
    print(f"Processed {len(nodes)} nodes and {len(edges)} edges")
    return nodes, edges

if __name__ == "__main__":
    process_data()
