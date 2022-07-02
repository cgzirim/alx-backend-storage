-- Creates a trigger that decreases the quantity of an item after adding a new order.
DROP TRIGGER IF EXISTS decrease_qty;

CREATE TRIGGER decrease_qty
AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - New.number
WHERE name = NEW.item_name;

