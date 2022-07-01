-- Creates a trigger that decreases the quantity of an item after adding a new order.
DROP TRIGGER IF EXISTS decrs_qty;

DELIMITER //
CREATE TRIGGER decrs_qty
AFTER INSERT ON orders FOR EACH ROW
BEGIN
	UPDATE items SET quantity = quantity - 2
	WHERE name = NEW.item_name;
END;
//
DELIMITER ;
