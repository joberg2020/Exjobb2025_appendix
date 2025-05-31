### Overview of example of generated modules and their objectives 
```json
{
  "id": "7cb2b13f-9523-4b44-9722-95d4103c31c0",
  "title": "Foundations of Basic Electronics",
  "description": "A concise series of modules designed to introduce the essential principles of electronics. Topics covered include the basics of electricity and circuits, identification and function of key electronic components, reading and drawing simple circuit diagrams, and applying Ohm’s Law to perform fundamental calculations.",
  "created_at": "2025-05-18T15:45:30.008773",
  "modules": [
    {
      "id": "9b352deb-e5b2-4eb0-8041-c40ddb318e75",
      "title": "Introduction to Electricity and Circuit Fundamentals",
      "objectives": [
        {
          "id": "e4fa6f3a-661a-4e22-8ea3-0b0d729f7d82",
          "text": "Define electricity and describe its fundamental properties."
        },
        {
          "id": "5d4577cb-5b4d-44a8-a0b6-ef215c105b2f",
          "text": "Distinguish between voltage, current, and resistance."
        },
        {
          "id": "942a642c-d9be-4bf4-bdc2-c191b4cec4d4",
          "text": "Explain the role and flow of electric charge in a simple circuit."
        },
        {
          "id": "78027a4f-4e03-4497-87a4-f988a9bcfa59",
          "text": "Identify the main components in a basic electrical circuit (source, conductor, load)."
        }
      ]
    },
    {
      "id": "afe10adc-4b57-4892-a3cb-5a8fe2961b69",
      "title": "Understanding Electronic Components",
      "objectives": [
        {
          "id": "1492dce3-9d99-4ccb-b424-28be6e4f4ec2",
          "text": "Identify and describe the function of basic electronic components such as resistors, capacitors, diodes, and switches."
        },
        {
          "id": "0f78add2-6fe3-4e65-a919-49ca494d2dab",
          "text": "Recognize schematic symbols for common components."
        },
        {
          "id": "deaeadae-27f2-4ea7-acfe-fd5c5df04d35",
          "text": "Explain the basic role of each component type in a simple circuit."
        }
      ]
    },
    {
      "id": "2be94727-2a1c-4d50-97be-5c54856fa645",
      "title": "Reading and Drawing Simple Circuit Diagrams",
      "objectives": [
        {
          "id": "f4482bbd-4baa-4fb8-8bea-520fd90042ed",
          "text": "Interpret basic electronic circuit diagrams and symbols."
        },
        {
          "id": "eeccacbf-aabb-4536-824a-94ba47693a35",
          "text": "Draw simple circuit schematics using standard symbols."
        },
        {
          "id": "f510770b-801d-42f0-b398-424779edcc82",
          "text": "Trace the flow of electricity through a given schematic."
        }
      ]
    },
    {
      "id": "79255661-42c0-459f-ac4f-fe049cfe5686",
      "title": "Applying Ohm’s Law and Basic Calculations",
      "objectives": [
        {
          "id": "52d585c2-3b33-4e27-bfcc-8b506a5c1212",
          "text": "State Ohm’s Law and its mathematical formula."
        },
        {
          "id": "a550db12-dc93-4409-aafb-246ec4305c19",
          "text": "Calculate current, voltage, and resistance in simple series and parallel circuits."
        },
        {
          "id": "ff6940d3-6ab2-4f70-adb5-e65bc4f9851a",
          "text": "Apply Ohm’s Law to solve basic circuit problems."
        }
      ]
    }
  ]
}
```
### Example of first modules knowledgebit (fluency aim not set yet):
```json
{
  "id": "9b352deb-e5b2-4eb0-8041-c40ddb318e75",
  "title": "Introduction to Electricity and Circuit Fundamentals",
  "description": "This module introduces the basic concepts of electricity, electrical charge, voltage, current, and circuits, which form the foundation for understanding electronics.",
  "series_id": "7cb2b13f-9523-4b44-9722-95d4103c31c0",
  "fluency_aim": null,
  "objectives": [
    {
      "id": "e4fa6f3a-661a-4e22-8ea3-0b0d729f7d82",
      "text": "Define electricity and describe its fundamental properties.",
      "seq_nr": 0,
      "knowledgebits": [
        {
          "id": "3dbef06b-86a5-43a9-a1a1-cd7449c90782",
          "content": "Electricity is the presence and flow of electric charge.",
          "explanation": "Electricity is simply about having and moving tiny particles with an electric charge.",
          "type": "fact"
        },
        {
          "id": "2c15ed89-1000-4b62-b2ad-f3f97c1b5a1d",
          "content": "The fundamental properties of electricity include charge, voltage, current, and resistance.",
          "explanation": "These are key features that help us understand how electricity works and behaves.",
          "type": "concept"
        },
        {
          "id": "de6c55d0-3c5b-46da-8d1c-d2cc9324aa13",
          "content": "Electric charge can be positive or negative.",
          "explanation": "Electric charge comes in two types: positive and negative, like a battery with a plus and minus side.",
          "type": "fact"
        },
        {
          "id": "a6b28486-763c-489e-af8a-49e6d7c34163",
          "content": "Electricity always seeks to flow from areas of high potential (voltage) to low potential.",
          "explanation": "Electrons move from places where there are a lot of them to places where there are fewer, like water flowing downhill.",
          "type": "principle"
        },
        {
          "id": "815e7e89-e08c-441a-a7da-1bd5c5bac032",
          "content": "Conductors are materials that allow electricity to flow easily, such as copper.",
          "explanation": "Conductors are like highways for electrical charge, letting it travel easily from one point to another.",
          "type": "fact"
        }
      ]
    },
    {
      "id": "5d4577cb-5b4d-44a8-a0b6-ef215c105b2f",
      "text": "Distinguish between voltage, current, and resistance.",
      "seq_nr": 1,
      "knowledgebits": [
        {
          "id": "892ea4d7-a6fb-4125-ab80-f003512ff240",
          "content": "Voltage is the measure of electric potential difference between two points.",
          "explanation": "Voltage is like the pressure that pushes electric charge through a circuit, similar to water pressure in pipes.",
          "type": "concept"
        },
        {
          "id": "a0b535c2-f2ee-4303-ad2a-869eb4db5acf",
          "content": "Current is the flow of electric charge in a circuit.",
          "explanation": "Current measures how much electric charge passes through a point in a circuit over time, like how much water flows through a pipe.",
          "type": "concept"
        },
        {
          "id": "0cee8606-e50e-40fb-b939-a56a1bc38a6b",
          "content": "Resistance is the opposition to the flow of electric current.",
          "explanation": "Resistance is like a bottleneck in a pipe that slows down the flow of water; it makes it harder for electricity to move.",
          "type": "concept"
        },
        {
          "id": "5d0460ca-f022-45d9-a02a-1ddd52a274a1",
          "content": "To measure voltage, current, and resistance, use a multimeter with the appropriate settings.",
          "explanation": "A multimeter can be adjusted to check how much voltage, current, or resistance there is in a circuit, like a Swiss army knife for electrical measurements.",
          "type": "sequence"
        },
        {
          "id": "af04a6b8-a466-425f-b7a9-ff9d61b2dbda",
          "content": "Increasing resistance in a circuit decreases the current flowing for a constant voltage.",
          "explanation": "If you add more resistance in a circuit without changing the voltage, less electricity will flow, much like adding obstacles that slow down water in a hose.",
          "type": "cause-and-effect"
        }
      ]
    },
    {
      "id": "942a642c-d9be-4bf4-bdc2-c191b4cec4d4",
      "text": "Explain the role and flow of electric charge in a simple circuit.",
      "seq_nr": 2,
      "knowledgebits": [
        {
          "id": "7e3e6cc9-9512-49cb-b547-42f67c144fab",
          "content": "Electric charge flows in a circuit from the negative terminal to the positive terminal of a power source.",
          "explanation": "Electric charge moves away from the negative side (where there's more charge) towards the positive side (where there's less charge) in a circuit.",
          "type": "concept"
        },
        {
          "id": "b99996b0-528b-41c3-a43f-692bcbd38b5a",
          "content": "In a simple circuit, the electric charge flows from the power source, through the conductor, to the load.",
          "explanation": "Charge travels in a loop starting at the battery, moving through wires, and powering a device like a light bulb.",
          "type": "sequence"
        },
        {
          "id": "7a782680-7025-416c-b00c-1d8f3a50f869",
          "content": "The flow of electric charge is measured in amperes (A).",
          "explanation": "Amperes measure how much electric charge is flowing in a circuit, like measuring gallons of water rushing through a pipe.",
          "type": "fact"
        },
        {
          "id": "3fba1396-4ca9-409e-b1ed-1184b79465f2",
          "content": "A circuit is a closed loop that allows electricity to flow continuously.",
          "explanation": "A circuit needs to be closed, like a racetrack, for electric charge to keep moving and power devices.",
          "type": "concept"
        },
        {
          "id": "e01772db-cacc-4b77-ab86-2c918ca896f6",
          "content": "Electric charge and energy must complete a circuit to do work, such as lighting a bulb.",
          "explanation": "For anything to work, like a light turning on, the charge has to keep going around in a complete loop without interruption.",
          "type": "principle"
        }
      ]
    },
    {
      "id": "78027a4f-4e03-4497-87a4-f988a9bcfa59",
      "text": "Identify the main components in a basic electrical circuit (source, conductor, load).",
      "seq_nr": 3,
      "knowledgebits": [
        {
          "id": "51ba8ba4-1897-446d-81e0-9bd94d530647",
          "content": "The main components of a basic electrical circuit are the power source, conductor, and load.",
          "explanation": "Every circuit has these three parts: a battery (power source), wires (conductors), and something that uses electricity, like a light bulb (load).",
          "type": "fact"
        },
        {
          "id": "5f27cbbc-ad6d-40cc-a3e5-244f9354f67a",
          "content": "The power source provides electrical energy to the circuit.",
          "explanation": "The power source is what 'feeds' the electricity needed to run things, like how batteries or outlets supply power.",
          "type": "concept"
        },
        {
          "id": "9389b20c-4f9b-441f-ab08-ec81fe2fe69b",
          "content": "A conductor is typically made from materials like copper or aluminum that allow electric charge to pass through.",
          "explanation": "Conductors are materials that let electricity flow easily, much like how certain types of pipes let water through quickly.",
          "type": "fact"
        },
        {
          "id": "898ecafc-43c3-4203-a7a9-3c4ec3d00374",
          "content": "A load is a component that uses electrical energy to perform work.",
          "explanation": "The load is anything powered by electricity, like a light bulb that lights up or a motor that spins.",
          "type": "concept"
        },
        {
          "id": "242d7b93-a565-4395-9913-99939d7cc4d5",
          "content": "Steps to identify components in a circuit include tracing wires from the power source to the load.",
          "explanation": "To find out what's in a circuit, follow the wires from where the power comes from to where it goes to do work.",
          "type": "sequence"
        }
      ]
    }
  ]
}
```
