#!/bin/bash

API_URL="http://127.0.0.1:8000/vehicles/"


VEHICLES=(
    '{"v_type": "van", "plate_number": "byteme" }'
    '{"v_type": "suv", "plate_number": "hondacrv" }'
    '{"v_type": "suv", "plate_number": "restful" }'
    '{"v_type": "suv", "plate_number": "djangoapp" }'
    '{"v_type": "sedan", "plate_number": "ilovejava" }'
    '{"v_type": "sedan", "plate_number": "gitcommit" }'
)

for VEHICLE in "${VEHICLES[@]}"; do
    echo "Posting: $VEHICLE"
    curl -X POST "$API_URL" -H "Content-Type: application/json" -d "$VEHICLE"

done
