import { ReactElement, ReactNode, useRef } from "react";
import { useLocalization, Localized } from "@fluent/react";
import {
  OverlayContainer,
  FocusScope,
  useDialog,
  useModal,
  useOverlay,
  usePreventScroll,
} from "react-aria";
import { OverlayProps } from "@react-aria/overlays";
import styles from "./ConfirmationModal.module.scss";
import checkIcon from "../../../../../static/images/icon-green-check.svg";
import partyIllustration from "../../../../../static/images/dashboard-onboarding/success-party.svg";
import { SubdomainConfirmationForm } from "./ConfirmationForm";
import { getRuntimeConfig } from "../../../config";
import { Button } from "../../Button";

export type Props = {
  subdomain: string;
  isOpen: boolean;
  isSet: boolean;
  onClose: () => void;
  onConfirm: () => void;
};

/**
 * Modal in which the user can confirm that they really want to permanently claim a given subdomain.
 */
export const SubdomainConfirmationModal = (props: Props) => {
  return !props.isSet ? (
    <OverlayContainer>
      <ConfirmModal {...props} />
    </OverlayContainer>
  ) : (
    <OverlayContainer>
      <SuccessModal {...props} />
    </OverlayContainer>
  );
};

const ConfirmModal = (props: Props) => {
  const { l10n } = useLocalization();

  return (
    <PickerDialog
      title={
        <Localized
          id="modal-domain-register-available-v2"
          vars={{
            subdomain: props.subdomain,
            domain: getRuntimeConfig().mozmailDomain,
          }}
          elems={{
            subdomain: <span className={styles.subdomain} />,
            domain: <span className={styles.domain} />,
          }}
        >
          <span className={styles.modalTitle} />
        </Localized>
      }
      headline={l10n.getString("modal-domain-register-good-news")}
      onClose={() => props.onClose()}
      isOpen={props.isOpen}
      isDismissable={true}
    >
      <SubdomainConfirmationForm
        subdomain={props.subdomain}
        onCancel={() => props.onClose()}
        onConfirm={() => props.onConfirm()}
      />
    </PickerDialog>
  );
};

const SuccessModal = (props: Props) => {
  const { l10n } = useLocalization();

  return (
    <div className={styles.pickedConfirmation}>
      <PickerDialog
        title={
          <Localized
            id="modal-domain-register-success-v2"
            vars={{
              subdomain: props.subdomain,
              domain: getRuntimeConfig().mozmailDomain,
            }}
            elems={{
              subdomain: <span className={styles.subdomain} />,
              domain: <span className={styles.domain} />,
            }}
          >
            <span className={styles.modalTitle} />
          </Localized>
        }
        headline={l10n.getString("modal-domain-register-success-title")}
        onClose={() => props.onClose()}
        isOpen={props.isOpen}
        isDismissable={true}
      >
        <div className={styles.pickedConfirmationBody}>
          <img src={partyIllustration.src} alt="" />
          <p>{l10n.getString("modal-domain-register-success-copy")}</p>
          <Button onClick={() => props.onClose()}>
            {l10n.getString("profile-label-continue")}
          </Button>
        </div>
      </PickerDialog>
    </div>
  );
};

type PickerDialogProps = {
  title: string | ReactElement;
  headline: string;
  children: ReactNode;
  isOpen: boolean;
  onClose?: () => void;
};
const PickerDialog = (props: PickerDialogProps & OverlayProps) => {
  const wrapperRef = useRef<HTMLDivElement>(null);
  const { overlayProps, underlayProps } = useOverlay(props, wrapperRef);
  usePreventScroll();
  const { modalProps } = useModal();
  const { dialogProps, titleProps } = useDialog({}, wrapperRef);

  return (
    <div className={styles.underlay} {...underlayProps}>
      <FocusScope contain restoreFocus autoFocus>
        <div
          className={styles.dialogWrapper}
          {...overlayProps}
          {...dialogProps}
          {...modalProps}
          ref={wrapperRef}
        >
          <div className={styles.hero}>
            <span className={styles.headline}>
              <img src={checkIcon.src} alt="" />
              {props.headline}
            </span>
            <h3 {...titleProps}>{props.title}</h3>
          </div>
          {props.children}
        </div>
      </FocusScope>
    </div>
  );
};
