import waste_detect as w
import matplotlib.pyplot as plt
def draw():
    plt.figure(figsize=(8,8))
    plt.scatter(w.y_valid.index, w.y_valid, color='blue', label='Actual Values', marker='o',alpha=0.5)
    plt.scatter(w.y_valid.index, w.y_pred, color='red', label='Predicted Values', marker='x',alpha=0.7)
    plt.xlabel('Data Point Index')
    plt.ylabel('Waste Category (Actual and Predicted)')
    plt.legend()
    plt.title('Actual vs. Predicted Waste Category')
    plt.show()