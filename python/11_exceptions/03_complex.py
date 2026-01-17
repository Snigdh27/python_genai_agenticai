def serve_chai(flavour):
    try:
        print(f"Serving {flavour} chai.")
        if flavour == "unknown":
            raise ValueError("Unknown chai flavour requested!")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"{flavour} chai served successfully.")
    finally:
        print("Thank you for visiting the chai shop.")

serve_chai("masala")
serve_chai("unknown")