import pyblish.api


class CollectUDIMs(pyblish.api.InstancePlugin):
    """Collect representations as UDIMs."""

    label = "Collect UDIMs"
    order = pyblish.api.CollectorOrder - 0.49
    hosts = ["traypublisher"]

    # TODO: Expose settings for profiles, and allow configuring from publisher
    #  UI if made optional in settings

    def process(self, instance):

        if not self.should_mark_instance_as_udim(instance):
            # Not defined to be marked as UDIM
            return

        representations = instance.data.get("representations", [])
        for repre in representations:
            if repre.get("udim"):
                # Already marked
                continue

            if not self.should_mark_representation_as_udim(repre):
                # Not defined to be marked as UDIM
                continue

            udims = self.collect_udims(repre)
            repre["udim"] = udims

    def should_mark_representation_as_udim(self, representation: dict) -> bool:
        """Check if representation should be marked as UDIM."""
        # TODO: Use profiles to match e.g. product name or product type
        #  or filter to e.g. only certain file types
        return True

    def should_mark_instance_as_udim(
            self,
            instance: pyblish.api.Instaance
    ) -> bool:
        """Check if instance should be marked as UDIM."""
        # TODO: Use profiles to match e.g. product name or product type
        return True

    def collect_udims(self, representation: dict) -> list[str]:
        """Collect UDIMs from representation."""
        # TODO: Implement collecting of udim sequence from the representation
        #  files.
        return ["1001", "1002", "1004"]